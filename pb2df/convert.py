# -*- coding: utf-8 -*-

import ctypes
from collections import namedtuple
from operator import attrgetter

from google.protobuf.descriptor import FieldDescriptor
from pyspark import RDD
from pyspark.sql import types

__all__ = ('convert_field', 'convert_schema', 'Converter')

CustomField = namedtuple('CustomField', ('type', 'converter'))

# type mapping between ProtoBuf and Spark SQL
_SPARK_SQL_TYPE_MAP = {
    FieldDescriptor.TYPE_DOUBLE: types.DoubleType(),
    FieldDescriptor.TYPE_FLOAT: types.FloatType(),
    FieldDescriptor.TYPE_INT32: types.IntegerType(),
    FieldDescriptor.TYPE_INT64: types.LongType(),
    FieldDescriptor.TYPE_UINT32: types.IntegerType(),
    FieldDescriptor.TYPE_UINT64: types.LongType(),
    FieldDescriptor.TYPE_SINT32: types.IntegerType(),
    FieldDescriptor.TYPE_SINT64: types.LongType(),
    FieldDescriptor.TYPE_FIXED32: types.IntegerType(),
    FieldDescriptor.TYPE_FIXED64: types.LongType(),
    FieldDescriptor.TYPE_SFIXED32: types.IntegerType(),
    FieldDescriptor.TYPE_SFIXED64: types.LongType(),
    FieldDescriptor.TYPE_BOOL: types.BooleanType(),
    FieldDescriptor.TYPE_STRING: types.StringType(),
    FieldDescriptor.TYPE_BYTES: types.BinaryType(),
    FieldDescriptor.TYPE_ENUM: types.IntegerType(),
}


def _to_int32(n):
    return ctypes.c_int32(n).value


def _to_int64(n):
    return ctypes.c_int64(n).value


def convert_field(pb_field, custom_fields=None):
    """Convert ProtoBuf field to Spark DataFrame field.

    Args:
      pb_field (`FieldDescriptor`): a single field in .proto file.

    Returns:
      A `(field, getter)` tuple, where

      - `field` represents a DataFrame field in a `StructField`, and
      - `getter` is a function which accepts a ProtoBuf object and extracts
        value of the given field.

    Note:
      Since there are no unsigned types in Spark SQL, if the type of field
      is unsigned integer (`uint32`, `uint64`, `fixed32`, or `fixed64`), it
      will be converted to its signed counterpart after extracting the value.

    Note:
      The getter for optional field with no default value will return `None` if
      this field is not set for the message.

    """

    field_converters = {}
    if custom_fields is not None:
        for k, v in custom_fields.items():
            try:
                field_name, sub_field_name = k.split('.', 1)
                custom_sub_fields = field_converters.setdefault(field_name, {})
                custom_sub_fields[sub_field_name] = v
            except ValueError:
                field_converters[k] = v

    field_name = pb_field.name
    field_label = pb_field.label
    field_type = pb_field.type
    is_field_nullable = field_label != FieldDescriptor.LABEL_REQUIRED
    is_repeated_field = field_label == FieldDescriptor.LABEL_REPEATED
    is_message_type = field_type == FieldDescriptor.TYPE_MESSAGE
    field_may_be_none = (field_label == FieldDescriptor.LABEL_OPTIONAL and
                         not pb_field.has_default_value)

    # generate field schema
    field_factory = None
    if is_message_type:
        df_field_type, field_factory = convert_schema(
            pb_field.message_type, field_converters.get(field_name))
    elif field_name in field_converters:
        df_field_type, field_factory = field_converters[field_name]
    else:
        df_field_type = _SPARK_SQL_TYPE_MAP[field_type]
        if isinstance(df_field_type, types.BinaryType):
            field_factory = bytearray
        elif isinstance(df_field_type, types.IntegerType):
            field_factory = _to_int32
        elif isinstance(df_field_type, types.LongType):
            field_factory = _to_int64

    if is_repeated_field:
        df_field_type = types.ArrayType(df_field_type, containsNull=False)

    field = types.StructField(field_name, df_field_type, is_field_nullable)

    # generate field getter
    # note: calling the accessor to get the value of an field which has not
    #       been explicitly set always returns that field's default value.
    if field_factory is None:
        if is_repeated_field:
            field_getter = lambda pb_obj: \
                list(getattr(pb_obj, field_name))
        else:
            field_getter = attrgetter(field_name)
    else:
        if is_repeated_field:
            field_getter = lambda pb_obj: \
                map(field_factory, getattr(pb_obj, field_name))
        else:
            field_getter = lambda pb_obj: \
                field_factory(getattr(pb_obj, field_name))

    if field_may_be_none:
        inner_field_getter = field_getter
        field_getter = lambda pb_obj: \
            inner_field_getter(pb_obj) if pb_obj.HasField(field_name) else None

    return field, field_getter


def convert_schema(pb_desc, custom_fields=None):
    """Convert ProtoBuf schema to Spark DataFrame schema.

    Args:
      pb_desc (`Descriptor`): a protocol message type.

    Returns:
      A `(schema, factory)` tuple, where

      - `schema` is represented by a `StructType`, and
      - `factory` is a function which accepts a ProtoBuf object and convert it
        to tuple.

    """

    field_schemas = []
    field_getters = []
    append_field_schema = field_schemas.append
    append_field_getter = field_getters.append
    for field in pb_desc.fields:
        schema, getter = convert_field(field, custom_fields)
        append_field_schema(schema)
        append_field_getter(getter)

    # note: `SQLContext.createDataFrame()` does not accept `namedtuple` or
    #       `dict` when the `schema` parameter is given; therefore, we just put
    #       all field values in a normal `tuple` instead of a `namedtuple`.
    def factory(pb_obj):
        return tuple(getter(pb_obj) for getter in field_getters)

    schema = types.StructType(field_schemas)
    return schema, factory


class Converter(object):

    def __init__(self, pb_msg_type, spark_ctx, sql_ctx, custom_fields=None):
        """Create an converter with given ProtoBuf message type.

        Args:
          pb_msg_type (`GeneratedProtocolMessageType`): a ProtoBuf message
            class which is used to generate the DataFrame schema.
          spark_ctx (`SparkContext`):
          sql_ctx (`SQLContext`): a `SQLContext` which is used to create
            DataFrame.

        """

        self._pb_msg_type = pb_msg_type
        self._spark_ctx = spark_ctx
        self._sql_ctx = sql_ctx
        self._schema, self._factory = convert_schema(
            pb_msg_type.DESCRIPTOR, custom_fields)

    def to_dataframe(self, pb_objs):
        """Convert a sequence of ProtoBuf objects to Spark DataFrame.

        Args:
          pb_objs (iterable of `Message`s or `RDD` of `Message`s): a sequence
            of ProtoBuf objects.

        Returns:
          A Spark DataFrame.

        """

        if not isinstance(pb_objs, RDD):
            pb_objs = self._spark_ctx.parallelize(pb_objs)

        # note: since `SQLContext.createDataFrame()` only accepts a sequence of
        #       `list`s/`tuple`s, we should convert each ProtoBuf object to
        #       tuple before passing it.
        tuples = pb_objs.map(self._factory)
        return self._sql_ctx.createDataFrame(tuples, schema=self._schema)
