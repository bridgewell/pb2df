# -*- coding: utf-8 -*-

import ctypes

import pyspark.sql

import example_pb2
import pb2df


def _test_schema(pb_msg_type, expected_schema):
    field_map = {field.name: field for field in expected_schema.fields}
    fields = pb_msg_type.DESCRIPTOR.fields_by_name
    for field_name, field_desc in fields.iteritems():
        field, _ = pb2df.convert_field(field_desc)
        assert field == field_map[field_name]

    schema, _ = pb2df.convert_schema(pb_msg_type.DESCRIPTOR)
    assert schema == expected_schema


def test_simple_msg_schema(simple_msg_schema):
    _test_schema(example_pb2.SimpleMessage, simple_msg_schema)


def test_basic_msg_schema(basic_msg_schema):
    _test_schema(example_pb2.BasicMessage, basic_msg_schema)


def test_labeled_msg_schema(labeled_msg_schema):
    _test_schema(example_pb2.LabeledMessage, labeled_msg_schema)


def test_nested_msg_schema(nested_msg_schema):
    _test_schema(example_pb2.NestedMessage, nested_msg_schema)


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


def test_nested_field_getter(nested_msg):
    pb_msg_type = nested_msg.__class__
    field_desc = pb_msg_type.DESCRIPTOR.fields_by_name['required_nested_field']

    _, getter = pb2df.convert_field(field_desc)
    _, factory = pb2df.convert_schema(field_desc.message_type)
    assert getter(nested_msg) == factory(nested_msg.required_nested_field)


def test_repeated_nested_field_getter(nested_msg):
    pb_msg_type = nested_msg.__class__
    field_desc = pb_msg_type.DESCRIPTOR.fields_by_name['repeated_nested_field']

    _, getter = pb2df.convert_field(field_desc)
    _, factory = pb2df.convert_schema(field_desc.message_type)
    assert getter(nested_msg) == map(factory, nested_msg.repeated_nested_field)


def test_basic_msg_factory(basic_msg):
    pb_msg_type = basic_msg.__class__
    fields = pb_msg_type.DESCRIPTOR.fields

    _, factory = pb2df.convert_schema(pb_msg_type.DESCRIPTOR)

    expected_values = tuple(getattr(basic_msg, field.name) for field in fields)
    assert factory(basic_msg) == expected_values


def test_nested_msg_factory(nested_msg):
    pb_msg_type = nested_msg.__class__

    _, factory = pb2df.convert_schema(pb_msg_type.DESCRIPTOR)

    expected_values = ((0,), (999,), [(1,), (2,)])
    assert factory(nested_msg) == expected_values


def test_basic_msg_dataframe(sql_ctx, basic_msg):
    pb_msg_type = basic_msg.__class__
    field_descs = pb_msg_type.DESCRIPTOR.fields

    uint32_set = frozenset(('uint32_field', 'fixed32_field'))
    uint64_set = frozenset(('uint64_field', 'fixed64_field'))

    converter = pb2df.Converter(sql_ctx, pb_msg_type)
    df = converter.to_dataframe([basic_msg])
    row = df.first()
    for field_desc in field_descs:
        field_name = field_desc.name
        expected_value = getattr(basic_msg, field_name)
        if field_name in uint32_set:
            expected_value = ctypes.c_int32(expected_value).value
        elif field_name in uint64_set:
            expected_value = ctypes.c_int64(expected_value).value

        assert getattr(row, field_name) == expected_value


def test_nested_msg_dataframe(sql_ctx, nested_msg):
    pb_msg_type = nested_msg.__class__
    converter = pb2df.Converter(sql_ctx, pb_msg_type)

    df = converter.to_dataframe([nested_msg])
    row = df.first()
    assert row.required_nested_field == pyspark.sql.Row(field=999)
    assert row.repeated_nested_field == [pyspark.sql.Row(field=1),
                                         pyspark.sql.Row(field=2)]
