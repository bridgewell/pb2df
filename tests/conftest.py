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

import pytest
from pyspark import SparkContext
from pyspark.sql import SQLContext, types

import example_pb2


@pytest.fixture(scope='session')
def sql_ctx():
    sc = SparkContext()
    return SQLContext(sc)


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
        types.StructField('bytes_field', types.StringType()),
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
def basic_msg():
    msg = example_pb2.BasicMessage()
    msg.double_field = ctypes.c_double(1.7e+308).value
    msg.float_field = ctypes.c_float(3.4e+38).value
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
    return msg


@pytest.fixture()
def nested_msg():
    msg = example_pb2.NestedMessage()
    msg.required_nested_field.field = 999
    inner_msg1 = msg.repeated_nested_field.add()
    inner_msg1.field = 1
    inner_msg2 = msg.repeated_nested_field.add()
    inner_msg2.field = 2
    return msg
