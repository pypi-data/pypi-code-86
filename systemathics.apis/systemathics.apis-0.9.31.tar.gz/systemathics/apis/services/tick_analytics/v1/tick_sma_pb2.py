# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick_analytics/v1/tick_sma.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='systemathics/apis/services/tick_analytics/v1/tick_sma.proto',
  package='systemathics.apis.services.tick_analytics.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;systemathics/apis/services/tick_analytics/v1/tick_sma.proto\x12,systemathics.apis.services.tick_analytics.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\"\x84\x03\n\x0eTickSmaRequest\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x42\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.Constraints\x12\x45\n\x05\x66ield\x18\x03 \x01(\x0e\x32\x36.systemathics.apis.services.tick_analytics.v1.SmaPrice\x12\x0e\n\x06length\x18\x04 \x01(\x05\x12)\n\x06period\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12)\n\x06offset\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x08sampling\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x12\n\nadjustment\x18\x08 \x01(\x08\"\x7f\n\x0fTickSmaResponse\x12.\n\ntime_stamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05value\x18\x02 \x01(\x01\x12-\n\x07\x61verage\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue*`\n\x08SmaPrice\x12\x19\n\x15SMA_PRICE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSMA_PRICE_TRADE\x10\x01\x12\x11\n\rSMA_PRICE_BID\x10\x02\x12\x11\n\rSMA_PRICE_ASK\x10\x03\x32\x9b\x01\n\x0eTickSmaService\x12\x88\x01\n\x07TickSma\x12<.systemathics.apis.services.tick_analytics.v1.TickSmaRequest\x1a=.systemathics.apis.services.tick_analytics.v1.TickSmaResponse0\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2.DESCRIPTOR,])

_SMAPRICE = _descriptor.EnumDescriptor(
  name='SmaPrice',
  full_name='systemathics.apis.services.tick_analytics.v1.SmaPrice',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SMA_PRICE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SMA_PRICE_TRADE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SMA_PRICE_BID', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SMA_PRICE_ASK', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=829,
  serialized_end=925,
)
_sym_db.RegisterEnumDescriptor(_SMAPRICE)

SmaPrice = enum_type_wrapper.EnumTypeWrapper(_SMAPRICE)
SMA_PRICE_UNSPECIFIED = 0
SMA_PRICE_TRADE = 1
SMA_PRICE_BID = 2
SMA_PRICE_ASK = 3



_TICKSMAREQUEST = _descriptor.Descriptor(
  name='TickSmaRequest',
  full_name='systemathics.apis.services.tick_analytics.v1.TickSmaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='systemathics.apis.services.tick_analytics.v1.TickSmaRequest.identifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='systemathics.apis.services.tick_analytics.v1.TickSmaRequest.constraints', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field', full_name='systemathics.apis.services.tick_analytics.v1.TickSmaRequest.field', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='systemathics.apis.services.tick_analytics.v1.TickSmaRequest.length', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='systemathics.apis.services.tick_analytics.v1.TickSmaRequest.period', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='systemathics.apis.services.tick_analytics.v1.TickSmaRequest.offset', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sampling', full_name='systemathics.apis.services.tick_analytics.v1.TickSmaRequest.sampling', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adjustment', full_name='systemathics.apis.services.tick_analytics.v1.TickSmaRequest.adjustment', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=310,
  serialized_end=698,
)


_TICKSMARESPONSE = _descriptor.Descriptor(
  name='TickSmaResponse',
  full_name='systemathics.apis.services.tick_analytics.v1.TickSmaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='systemathics.apis.services.tick_analytics.v1.TickSmaResponse.time_stamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='systemathics.apis.services.tick_analytics.v1.TickSmaResponse.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='average', full_name='systemathics.apis.services.tick_analytics.v1.TickSmaResponse.average', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=700,
  serialized_end=827,
)

_TICKSMAREQUEST.fields_by_name['identifier'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2._IDENTIFIER
_TICKSMAREQUEST.fields_by_name['constraints'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2._CONSTRAINTS
_TICKSMAREQUEST.fields_by_name['field'].enum_type = _SMAPRICE
_TICKSMAREQUEST.fields_by_name['period'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TICKSMAREQUEST.fields_by_name['offset'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TICKSMAREQUEST.fields_by_name['sampling'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TICKSMARESPONSE.fields_by_name['time_stamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TICKSMARESPONSE.fields_by_name['average'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
DESCRIPTOR.message_types_by_name['TickSmaRequest'] = _TICKSMAREQUEST
DESCRIPTOR.message_types_by_name['TickSmaResponse'] = _TICKSMARESPONSE
DESCRIPTOR.enum_types_by_name['SmaPrice'] = _SMAPRICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TickSmaRequest = _reflection.GeneratedProtocolMessageType('TickSmaRequest', (_message.Message,), {
  'DESCRIPTOR' : _TICKSMAREQUEST,
  '__module__' : 'systemathics.apis.services.tick_analytics.v1.tick_sma_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.tick_analytics.v1.TickSmaRequest)
  })
_sym_db.RegisterMessage(TickSmaRequest)

TickSmaResponse = _reflection.GeneratedProtocolMessageType('TickSmaResponse', (_message.Message,), {
  'DESCRIPTOR' : _TICKSMARESPONSE,
  '__module__' : 'systemathics.apis.services.tick_analytics.v1.tick_sma_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.tick_analytics.v1.TickSmaResponse)
  })
_sym_db.RegisterMessage(TickSmaResponse)



_TICKSMASERVICE = _descriptor.ServiceDescriptor(
  name='TickSmaService',
  full_name='systemathics.apis.services.tick_analytics.v1.TickSmaService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=928,
  serialized_end=1083,
  methods=[
  _descriptor.MethodDescriptor(
    name='TickSma',
    full_name='systemathics.apis.services.tick_analytics.v1.TickSmaService.TickSma',
    index=0,
    containing_service=None,
    input_type=_TICKSMAREQUEST,
    output_type=_TICKSMARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TICKSMASERVICE)

DESCRIPTOR.services_by_name['TickSmaService'] = _TICKSMASERVICE

# @@protoc_insertion_point(module_scope)
