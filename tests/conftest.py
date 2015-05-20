# -*- coding: utf-8 -*-

import os
import sys

try:
    sys.path.append(os.path.join(
        os.environ['SPARK_HOME'], 'python'))
    sys.path.append(os.path.join(
        os.environ['SPARK_HOME'], 'python', 'lib', 'py4j-0.8.2.1-src.zip'))
except KeyError:
    raise Exception('$SPARK_HOME not set')

import ctypes
from datetime import datetime

import pytest
from pyspark import SparkContext
from pyspark.sql import SQLContext, types

import example_pb2


def _to_timestamp(dt):
    return (dt - datetime(1970, 1, 1)).total_seconds()


@pytest.fixture(scope='session')
def spark_ctx():
    return SparkContext()


@pytest.fixture(scope='session')
def sql_ctx(spark_ctx):
    return SQLContext(spark_ctx)


@pytest.fixture()
def simple_msg_schema():
    schema = types.StructType([
        types.StructField('field', types.IntegerType()),
    ])
    return schema


@pytest.fixture()
def basic_msg_schema():
    schema = types.StructType([
        types.StructField('double_field', types.DoubleType()),
        types.StructField('float_field', types.FloatType()),
        types.StructField('int32_field', types.IntegerType()),
        types.StructField('int64_field', types.LongType()),
        types.StructField('uint32_field', types.IntegerType()),
        types.StructField('uint64_field', types.LongType()),
        types.StructField('sint32_field', types.IntegerType()),
        types.StructField('sint64_field', types.LongType()),
        types.StructField('fixed32_field', types.IntegerType()),
        types.StructField('fixed64_field', types.LongType()),
        types.StructField('sfixed32_field', types.IntegerType()),
        types.StructField('sfixed64_field', types.LongType()),
        types.StructField('bool_field', types.BooleanType()),
        types.StructField('string_field', types.StringType()),
        types.StructField('bytes_field', types.BinaryType()),
        types.StructField('enum_field', types.IntegerType()),
    ])
    return schema


@pytest.fixture()
def labeled_msg_schema():
    schema = types.StructType([
        types.StructField('optional_field', types.BooleanType()),
        types.StructField('required_field', types.DoubleType(),
                          nullable=False),
        types.StructField('repeated_field', types.ArrayType(
            types.IntegerType(), containsNull=False)),
        types.StructField('default_field', types.StringType()),
    ])
    return schema


@pytest.fixture()
def nested_msg_schema(simple_msg_schema):
    schema = types.StructType([
        types.StructField('optional_nested_field', simple_msg_schema),
        types.StructField('required_nested_field', simple_msg_schema,
                          nullable=False),
        types.StructField('repeated_nested_field', types.ArrayType(
            simple_msg_schema, containsNull=False)),
    ])
    return schema


@pytest.fixture()
def custom_field_msg_schema():
    schema = types.StructType([
        types.StructField('timestamp_field', types.TimestampType(),
                          nullable=False),
    ])
    return schema


@pytest.fixture()
def basic_msg():
    msg = example_pb2.BasicMessage()
    msg.double_field = 1.7e+308
    msg.float_field = 3.4e+38
    msg.int32_field = 2 ** 31 - 1
    msg.int64_field = 2 ** 63 - 1
    msg.uint32_field = 2 ** 32 - 1
    msg.uint64_field = 2 ** 64 - 1
    msg.sint32_field = -2 ** 31
    msg.sint64_field = -2 ** 63
    msg.fixed32_field = 1234567890
    msg.fixed64_field = 9876543210
    msg.sfixed32_field = -1234567890
    msg.sfixed64_field = -9876543210
    msg.bool_field = True
    msg.string_field = 'string'
    msg.bytes_field = b'\x00\x01\x02\x03\x04'
    msg.enum_field = example_pb2.BasicMessage.ITEM_2
    msg.ParseFromString(msg.SerializeToString())
    return msg


@pytest.fixture()
def labeled_msg():
    msg = example_pb2.LabeledMessage()
    msg.optional_field = True
    msg.required_field = 1.414
    msg.repeated_field.append(1)
    msg.repeated_field.append(2)
    msg.repeated_field.append(3)
    msg.repeated_field.append(4)
    # ignore msg.default_field
    msg.ParseFromString(msg.SerializeToString())
    return msg


@pytest.fixture()
def nested_msg():
    msg = example_pb2.NestedMessage()
    # ignore msg.optional_nested_field
    msg.required_nested_field.field = 999
    inner_msg1 = msg.repeated_nested_field.add()
    inner_msg1.field = 1
    inner_msg2 = msg.repeated_nested_field.add()
    inner_msg2.field = 2
    msg.ParseFromString(msg.SerializeToString())
    return msg


@pytest.fixture()
def custom_field_msg():
    msg = example_pb2.CustomFieldMessage()
    msg.timestamp_field = _to_timestamp(datetime(2015, 04, 01, 12, 30))
    return msg


@pytest.fixture()
def basic_msg_tuple():
    values = (
        1.7e+308,  # double_field
        ctypes.c_float(3.4e+38).value,  # float_field
        2 ** 31 - 1,  # int32_field
        2 ** 63 - 1,  # int64_field
        ctypes.c_int32(2 ** 32 - 1).value,  # uint32_field
        ctypes.c_int64(2 ** 64 - 1).value,  # uint64_field
        -2 ** 31,  # sint32_field
        -2 ** 63,  # sint64_field
        ctypes.c_int32(1234567890).value,  # fixed32_field
        ctypes.c_int64(9876543210).value,  # fixed64_field
        -1234567890,  # sfixed32_field
        -9876543210,  # sfixed64_field
        True,  # bool_field
        'string',  # string_field
        bytearray(b'\x00\x01\x02\x03\x04'),  # bytes_field
        example_pb2.BasicMessage.ITEM_2,  # enum_field
    )
    return values


@pytest.fixture()
def nested_msg_tuple():
    return (None, (999,), [(1,), (2,)])


@pytest.fixture()
def custom_field_msg_tuple():
    return (datetime(2015, 04, 01, 12, 30),)
