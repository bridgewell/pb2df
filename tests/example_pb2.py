# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='example',
  serialized_pb='\n\rexample.proto\x12\x07\x65xample\"\x1e\n\rSimpleMessage\x12\r\n\x05\x66ield\x18\x01 \x01(\x05\"\xb4\x03\n\x0c\x42\x61sicMessage\x12\x14\n\x0c\x64ouble_field\x18\x01 \x01(\x01\x12\x13\n\x0b\x66loat_field\x18\x02 \x01(\x02\x12\x13\n\x0bint32_field\x18\x03 \x01(\x05\x12\x13\n\x0bint64_field\x18\x04 \x01(\x03\x12\x14\n\x0cuint32_field\x18\x05 \x01(\r\x12\x14\n\x0cuint64_field\x18\x06 \x01(\x04\x12\x14\n\x0csint32_field\x18\x07 \x01(\x11\x12\x14\n\x0csint64_field\x18\x08 \x01(\x12\x12\x15\n\rfixed32_field\x18\t \x01(\x07\x12\x15\n\rfixed64_field\x18\n \x01(\x06\x12\x16\n\x0esfixed32_field\x18\x0b \x01(\x0f\x12\x16\n\x0esfixed64_field\x18\x0c \x01(\x10\x12\x12\n\nbool_field\x18\r \x01(\x08\x12\x14\n\x0cstring_field\x18\x0e \x01(\t\x12\x13\n\x0b\x62ytes_field\x18\x0f \x01(\x0c\x12.\n\nenum_field\x18\x10 \x01(\x0e\x32\x1a.example.BasicMessage.Enum\"*\n\x04\x45num\x12\n\n\x06ITEM_0\x10\x00\x12\n\n\x06ITEM_1\x10\x01\x12\n\n\x06ITEM_2\x10\x02\"x\n\x0eLabeledMessage\x12\x16\n\x0eoptional_field\x18\x01 \x01(\x08\x12\x16\n\x0erequired_field\x18\x02 \x02(\x01\x12\x16\n\x0erepeated_field\x18\x03 \x03(\x05\x12\x1e\n\rdefault_field\x18\x04 \x01(\t:\x07\x64\x65\x66\x61ult\"\xb4\x01\n\rNestedMessage\x12\x35\n\x15optional_nested_field\x18\x01 \x01(\x0b\x32\x16.example.SimpleMessage\x12\x35\n\x15required_nested_field\x18\x02 \x02(\x0b\x32\x16.example.SimpleMessage\x12\x35\n\x15repeated_nested_field\x18\x03 \x03(\x0b\x32\x16.example.SimpleMessage\"-\n\x12\x43ustomFieldMessage\x12\x17\n\x0ftimestamp_field\x18\x01 \x02(\x01')



_BASICMESSAGE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='example.BasicMessage.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ITEM_0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_1', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_2', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=453,
  serialized_end=495,
)


_SIMPLEMESSAGE = _descriptor.Descriptor(
  name='SimpleMessage',
  full_name='example.SimpleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='example.SimpleMessage.field', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=26,
  serialized_end=56,
)


_BASICMESSAGE = _descriptor.Descriptor(
  name='BasicMessage',
  full_name='example.BasicMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='double_field', full_name='example.BasicMessage.double_field', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_field', full_name='example.BasicMessage.float_field', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int32_field', full_name='example.BasicMessage.int32_field', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int64_field', full_name='example.BasicMessage.int64_field', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint32_field', full_name='example.BasicMessage.uint32_field', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint64_field', full_name='example.BasicMessage.uint64_field', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sint32_field', full_name='example.BasicMessage.sint32_field', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sint64_field', full_name='example.BasicMessage.sint64_field', index=7,
      number=8, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fixed32_field', full_name='example.BasicMessage.fixed32_field', index=8,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fixed64_field', full_name='example.BasicMessage.fixed64_field', index=9,
      number=10, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sfixed32_field', full_name='example.BasicMessage.sfixed32_field', index=10,
      number=11, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sfixed64_field', full_name='example.BasicMessage.sfixed64_field', index=11,
      number=12, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bool_field', full_name='example.BasicMessage.bool_field', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_field', full_name='example.BasicMessage.string_field', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_field', full_name='example.BasicMessage.bytes_field', index=14,
      number=15, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enum_field', full_name='example.BasicMessage.enum_field', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BASICMESSAGE_ENUM,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=59,
  serialized_end=495,
)


_LABELEDMESSAGE = _descriptor.Descriptor(
  name='LabeledMessage',
  full_name='example.LabeledMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optional_field', full_name='example.LabeledMessage.optional_field', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required_field', full_name='example.LabeledMessage.required_field', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeated_field', full_name='example.LabeledMessage.repeated_field', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_field', full_name='example.LabeledMessage.default_field', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("default", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=497,
  serialized_end=617,
)


_NESTEDMESSAGE = _descriptor.Descriptor(
  name='NestedMessage',
  full_name='example.NestedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optional_nested_field', full_name='example.NestedMessage.optional_nested_field', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required_nested_field', full_name='example.NestedMessage.required_nested_field', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeated_nested_field', full_name='example.NestedMessage.repeated_nested_field', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=620,
  serialized_end=800,
)


_CUSTOMFIELDMESSAGE = _descriptor.Descriptor(
  name='CustomFieldMessage',
  full_name='example.CustomFieldMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_field', full_name='example.CustomFieldMessage.timestamp_field', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=802,
  serialized_end=847,
)

_BASICMESSAGE.fields_by_name['enum_field'].enum_type = _BASICMESSAGE_ENUM
_BASICMESSAGE_ENUM.containing_type = _BASICMESSAGE;
_NESTEDMESSAGE.fields_by_name['optional_nested_field'].message_type = _SIMPLEMESSAGE
_NESTEDMESSAGE.fields_by_name['required_nested_field'].message_type = _SIMPLEMESSAGE
_NESTEDMESSAGE.fields_by_name['repeated_nested_field'].message_type = _SIMPLEMESSAGE
DESCRIPTOR.message_types_by_name['SimpleMessage'] = _SIMPLEMESSAGE
DESCRIPTOR.message_types_by_name['BasicMessage'] = _BASICMESSAGE
DESCRIPTOR.message_types_by_name['LabeledMessage'] = _LABELEDMESSAGE
DESCRIPTOR.message_types_by_name['NestedMessage'] = _NESTEDMESSAGE
DESCRIPTOR.message_types_by_name['CustomFieldMessage'] = _CUSTOMFIELDMESSAGE

class SimpleMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIMPLEMESSAGE

  # @@protoc_insertion_point(class_scope:example.SimpleMessage)

class BasicMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BASICMESSAGE

  # @@protoc_insertion_point(class_scope:example.BasicMessage)

class LabeledMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LABELEDMESSAGE

  # @@protoc_insertion_point(class_scope:example.LabeledMessage)

class NestedMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NESTEDMESSAGE

  # @@protoc_insertion_point(class_scope:example.NestedMessage)

class CustomFieldMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CUSTOMFIELDMESSAGE

  # @@protoc_insertion_point(class_scope:example.CustomFieldMessage)


# @@protoc_insertion_point(module_scope)
