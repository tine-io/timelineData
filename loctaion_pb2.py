# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loctaion.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='loctaion.proto',
  package='location',
  syntax='proto3',
  serialized_options=b'\n\031io.grpc.examples.locationB\rLocationProtoP\001\242\002\003LOC',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eloctaion.proto\x12\x08location\"+\n\x16LocationByTimestampReq\x12\x11\n\ttimestamp\x18\x01 \x01(\x05\"*\n\rLocationReply\x12\x0b\n\x03lat\x18\x01 \x01(\x05\x12\x0c\n\x04long\x18\x02 \x01(\x05\x32\x61\n\x08Location\x12U\n\x16GetLocationByTimestamp\x12 .location.LocationByTimestampReq\x1a\x17.location.LocationReply\"\x00\x42\x32\n\x19io.grpc.examples.locationB\rLocationProtoP\x01\xa2\x02\x03LOCb\x06proto3'
)




_LOCATIONBYTIMESTAMPREQ = _descriptor.Descriptor(
  name='LocationByTimestampReq',
  full_name='location.LocationByTimestampReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='location.LocationByTimestampReq.timestamp', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=71,
)


_LOCATIONREPLY = _descriptor.Descriptor(
  name='LocationReply',
  full_name='location.LocationReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='location.LocationReply.lat', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='long', full_name='location.LocationReply.long', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['LocationByTimestampReq'] = _LOCATIONBYTIMESTAMPREQ
DESCRIPTOR.message_types_by_name['LocationReply'] = _LOCATIONREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationByTimestampReq = _reflection.GeneratedProtocolMessageType('LocationByTimestampReq', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONBYTIMESTAMPREQ,
  '__module__' : 'loctaion_pb2'
  # @@protoc_insertion_point(class_scope:location.LocationByTimestampReq)
  })
_sym_db.RegisterMessage(LocationByTimestampReq)

LocationReply = _reflection.GeneratedProtocolMessageType('LocationReply', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONREPLY,
  '__module__' : 'loctaion_pb2'
  # @@protoc_insertion_point(class_scope:location.LocationReply)
  })
_sym_db.RegisterMessage(LocationReply)


DESCRIPTOR._options = None

_LOCATION = _descriptor.ServiceDescriptor(
  name='Location',
  full_name='location.Location',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=117,
  serialized_end=214,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLocationByTimestamp',
    full_name='location.Location.GetLocationByTimestamp',
    index=0,
    containing_service=None,
    input_type=_LOCATIONBYTIMESTAMPREQ,
    output_type=_LOCATIONREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCATION)

DESCRIPTOR.services_by_name['Location'] = _LOCATION

# @@protoc_insertion_point(module_scope)