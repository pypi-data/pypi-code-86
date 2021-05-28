# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily_analytics/v1/daily_rsi.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import date_pb2 as google_dot_type_dot_date__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='systemathics/apis/services/daily_analytics/v1/daily_rsi.proto',
  package='systemathics.apis.services.daily_analytics.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=systemathics/apis/services/daily_analytics/v1/daily_rsi.proto\x12-systemathics.apis.services.daily_analytics.v1\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\"\xa7\x01\n\x0f\x44\x61ilyRsiRequest\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x42\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.Constraints\x12\x0e\n\x06length\x18\x03 \x01(\x05\"]\n\x10\x44\x61ilyRsiResponse\x12I\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32;.systemathics.apis.services.daily_analytics.v1.DailyRsiData\"K\n\x0c\x44\x61ilyRsiData\x12\x1f\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.Date\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x0b\n\x03rsi\x18\x03 \x01(\x01\x32\x9f\x01\n\x0f\x44\x61ilyRsiService\x12\x8b\x01\n\x08\x44\x61ilyRsi\x12>.systemathics.apis.services.daily_analytics.v1.DailyRsiRequest\x1a?.systemathics.apis.services.daily_analytics.v1.DailyRsiResponseb\x06proto3'
  ,
  dependencies=[google_dot_type_dot_date__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2.DESCRIPTOR,])




_DAILYRSIREQUEST = _descriptor.Descriptor(
  name='DailyRsiRequest',
  full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiRequest.identifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiRequest.constraints', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiRequest.length', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=240,
  serialized_end=407,
)


_DAILYRSIRESPONSE = _descriptor.Descriptor(
  name='DailyRsiResponse',
  full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=409,
  serialized_end=502,
)


_DAILYRSIDATA = _descriptor.Descriptor(
  name='DailyRsiData',
  full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiData.date', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiData.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rsi', full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiData.rsi', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=504,
  serialized_end=579,
)

_DAILYRSIREQUEST.fields_by_name['identifier'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2._IDENTIFIER
_DAILYRSIREQUEST.fields_by_name['constraints'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2._CONSTRAINTS
_DAILYRSIRESPONSE.fields_by_name['data'].message_type = _DAILYRSIDATA
_DAILYRSIDATA.fields_by_name['date'].message_type = google_dot_type_dot_date__pb2._DATE
DESCRIPTOR.message_types_by_name['DailyRsiRequest'] = _DAILYRSIREQUEST
DESCRIPTOR.message_types_by_name['DailyRsiResponse'] = _DAILYRSIRESPONSE
DESCRIPTOR.message_types_by_name['DailyRsiData'] = _DAILYRSIDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyRsiRequest = _reflection.GeneratedProtocolMessageType('DailyRsiRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYRSIREQUEST,
  '__module__' : 'systemathics.apis.services.daily_analytics.v1.daily_rsi_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily_analytics.v1.DailyRsiRequest)
  })
_sym_db.RegisterMessage(DailyRsiRequest)

DailyRsiResponse = _reflection.GeneratedProtocolMessageType('DailyRsiResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYRSIRESPONSE,
  '__module__' : 'systemathics.apis.services.daily_analytics.v1.daily_rsi_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily_analytics.v1.DailyRsiResponse)
  })
_sym_db.RegisterMessage(DailyRsiResponse)

DailyRsiData = _reflection.GeneratedProtocolMessageType('DailyRsiData', (_message.Message,), {
  'DESCRIPTOR' : _DAILYRSIDATA,
  '__module__' : 'systemathics.apis.services.daily_analytics.v1.daily_rsi_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily_analytics.v1.DailyRsiData)
  })
_sym_db.RegisterMessage(DailyRsiData)



_DAILYRSISERVICE = _descriptor.ServiceDescriptor(
  name='DailyRsiService',
  full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=582,
  serialized_end=741,
  methods=[
  _descriptor.MethodDescriptor(
    name='DailyRsi',
    full_name='systemathics.apis.services.daily_analytics.v1.DailyRsiService.DailyRsi',
    index=0,
    containing_service=None,
    input_type=_DAILYRSIREQUEST,
    output_type=_DAILYRSIRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DAILYRSISERVICE)

DESCRIPTOR.services_by_name['DailyRsiService'] = _DAILYRSISERVICE

# @@protoc_insertion_point(module_scope)
