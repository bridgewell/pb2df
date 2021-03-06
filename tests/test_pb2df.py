# -*- coding: utf-8 -*-

from datetime import datetime

import pyspark.sql
from pyspark.sql import types

import example_pb2
import pb2df.convert as pb2df


def _test_schema(pb_msg_type, expected_schema, custom_fields=None):
    field_map = {field.name: field for field in expected_schema.fields}
    fields = pb_msg_type.DESCRIPTOR.fields_by_name
    for field_name, field_desc in fields.iteritems():
        field, _ = pb2df.convert_field(field_desc, custom_fields)
        assert field == field_map[field_name]

    schema, _ = pb2df.convert_schema(pb_msg_type.DESCRIPTOR, custom_fields)
    assert schema == expected_schema


def test_simple_msg_schema(simple_msg_schema):
    _test_schema(example_pb2.SimpleMessage, simple_msg_schema)


def test_basic_msg_schema(basic_msg_schema):
    _test_schema(example_pb2.BasicMessage, basic_msg_schema)


def test_labeled_msg_schema(labeled_msg_schema):
    _test_schema(example_pb2.LabeledMessage, labeled_msg_schema)


def test_nested_msg_schema(nested_msg_schema):
    _test_schema(example_pb2.NestedMessage, nested_msg_schema)


def test_custom_field_msg_schema(custom_field_msg_schema):
    custom_fields = {
        'timestamp_field': pb2df.CustomField(
            types.TimestampType(), datetime.utcfromtimestamp),
    }
    _test_schema(example_pb2.CustomFieldMessage, custom_field_msg_schema,
                 custom_fields)


def test_basic_field_getter(basic_msg):
    pb_msg_type = basic_msg.__class__
    field_desc = pb_msg_type.DESCRIPTOR.fields_by_name['double_field']
    _, getter = pb2df.convert_field(field_desc)
    assert getter(basic_msg) == basic_msg.double_field


def test_repeated_field_getter(labeled_msg):
    pb_msg_type = labeled_msg.__class__
    field_desc = pb_msg_type.DESCRIPTOR.fields_by_name['repeated_field']
    _, getter = pb2df.convert_field(field_desc)
    assert getter(labeled_msg) == labeled_msg.repeated_field


def test_default_field_getter():
    pb_msg_type = example_pb2.LabeledMessage
    field_desc = pb_msg_type.DESCRIPTOR.fields_by_name['default_field']
    _, getter = pb2df.convert_field(field_desc)
    assert getter(pb_msg_type()) == field_desc.default_value


def test_empty_field_getter():
    pb_msg_type = example_pb2.SimpleMessage
    field_desc = pb_msg_type.DESCRIPTOR.fields_by_name['field']
    _, getter = pb2df.convert_field(field_desc)
    assert getter(pb_msg_type()) is None


def test_nested_field_getter(nested_msg):
    pb_msg_type = nested_msg.__class__
    field_desc = pb_msg_type.DESCRIPTOR.fields_by_name['required_nested_field']
    _, getter = pb2df.convert_field(field_desc)
    assert getter(nested_msg) == (999,)


def test_repeated_nested_field_getter(nested_msg):
    pb_msg_type = nested_msg.__class__
    field_desc = pb_msg_type.DESCRIPTOR.fields_by_name['repeated_nested_field']
    _, getter = pb2df.convert_field(field_desc)
    assert getter(nested_msg) == [(1,), (2,)]


def test_custom_field_getter(custom_field_msg):
    convert = datetime.utcfromtimestamp
    custom_fields = {
        'timestamp_field': pb2df.CustomField(
            types.TimestampType(), convert),
    }
    pb_msg_type = custom_field_msg.__class__
    field_desc = pb_msg_type.DESCRIPTOR.fields_by_name['timestamp_field']
    _, getter = pb2df.convert_field(field_desc, custom_fields)
    assert getter(custom_field_msg) == convert(custom_field_msg.timestamp_field)


def test_basic_msg_factory(basic_msg, basic_msg_tuple):
    pb_msg_type = basic_msg.__class__
    _, factory = pb2df.convert_schema(pb_msg_type.DESCRIPTOR)
    assert factory(basic_msg) == basic_msg_tuple


def test_nested_msg_factory(nested_msg, nested_msg_tuple):
    pb_msg_type = nested_msg.__class__
    _, factory = pb2df.convert_schema(pb_msg_type.DESCRIPTOR)
    assert factory(nested_msg) == nested_msg_tuple


def test_custom_field_msg_factory(custom_field_msg, custom_field_msg_tuple):
    custom_fields = {
        'timestamp_field': pb2df.CustomField(
            types.TimestampType(), datetime.utcfromtimestamp),
    }
    pb_msg_type = custom_field_msg.__class__
    _, factory = pb2df.convert_schema(pb_msg_type.DESCRIPTOR, custom_fields)
    assert factory(custom_field_msg) == custom_field_msg_tuple


def test_empty_msg_dataframe(spark_ctx, sql_ctx):
    pb_msg_type = example_pb2.SimpleMessage
    converter = pb2df.Converter(pb_msg_type, spark_ctx, sql_ctx)
    df = converter.to_dataframe([pb_msg_type()])
    row = df.first()
    assert tuple(row) == (None,)


def test_basic_msg_dataframe(spark_ctx, sql_ctx, basic_msg, basic_msg_tuple):
    pb_msg_type = basic_msg.__class__
    converter = pb2df.Converter(pb_msg_type, spark_ctx, sql_ctx)
    df = converter.to_dataframe([basic_msg])
    row = df.first()
    assert tuple(row) == basic_msg_tuple


def test_nested_msg_dataframe(spark_ctx, sql_ctx, nested_msg):
    pb_msg_type = nested_msg.__class__
    converter = pb2df.Converter(pb_msg_type, spark_ctx, sql_ctx)
    df = converter.to_dataframe([nested_msg])
    row = df.first()
    assert row.optional_nested_field is None
    assert row.required_nested_field == pyspark.sql.Row(field=999)
    assert row.repeated_nested_field == [pyspark.sql.Row(field=1),
                                         pyspark.sql.Row(field=2)]


def test_custom_field_msg_dataframe(spark_ctx, sql_ctx, custom_field_msg,
                                    custom_field_msg_tuple):
    fts = (lambda x: datetime.utcfromtimestamp(x))
    custom_fields = {
        'timestamp_field': pb2df.CustomField(types.TimestampType(), fts),
    }
    pb_msg_type = custom_field_msg.__class__
    converter = pb2df.Converter(pb_msg_type, spark_ctx, sql_ctx, custom_fields)
    df = converter.to_dataframe([custom_field_msg])
    row = df.first()
    assert tuple(row) == custom_field_msg_tuple
