# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/type/shared/v1/constraints.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import date_pb2 as google_dot_type_dot_date__pb2
from google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
from systemathics.apis.type.shared.v1 import date_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2
from systemathics.apis.type.shared.v1 import time_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_time__interval__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='systemathics/apis/type/shared/v1/constraints.proto',
  package='systemathics.apis.type.shared.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2systemathics/apis/type/shared/v1/constraints.proto\x12 systemathics.apis.type.shared.v1\x1a\x16google/type/date.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\x1a\x34systemathics/apis/type/shared/v1/time_interval.proto\"\xf7\x01\n\x0b\x43onstraints\x12\x46\n\x0e\x64\x61te_intervals\x18\x01 \x03(\x0b\x32..systemathics.apis.type.shared.v1.DateInterval\x12\x46\n\x0etime_intervals\x18\x02 \x03(\x0b\x32..systemathics.apis.type.shared.v1.TimeInterval\x12)\n\x0e\x65xcluded_dates\x18\x03 \x03(\x0b\x32\x11.google.type.Date\x12-\n\rexcluded_days\x18\x04 \x03(\x0e\x32\x16.google.type.DayOfWeekb\x06proto3'
  ,
  dependencies=[google_dot_type_dot_date__pb2.DESCRIPTOR,google_dot_type_dot_dayofweek__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_time__interval__pb2.DESCRIPTOR,])




_CONSTRAINTS = _descriptor.Descriptor(
  name='Constraints',
  full_name='systemathics.apis.type.shared.v1.Constraints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date_intervals', full_name='systemathics.apis.type.shared.v1.Constraints.date_intervals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_intervals', full_name='systemathics.apis.type.shared.v1.Constraints.time_intervals', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='excluded_dates', full_name='systemathics.apis.type.shared.v1.Constraints.excluded_dates', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='excluded_days', full_name='systemathics.apis.type.shared.v1.Constraints.excluded_days', index=3,
      number=4, type=14, cpp_type=8, label=3,
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
  serialized_start=250,
  serialized_end=497,
)

_CONSTRAINTS.fields_by_name['date_intervals'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2._DATEINTERVAL
_CONSTRAINTS.fields_by_name['time_intervals'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_time__interval__pb2._TIMEINTERVAL
_CONSTRAINTS.fields_by_name['excluded_dates'].message_type = google_dot_type_dot_date__pb2._DATE
_CONSTRAINTS.fields_by_name['excluded_days'].enum_type = google_dot_type_dot_dayofweek__pb2._DAYOFWEEK
DESCRIPTOR.message_types_by_name['Constraints'] = _CONSTRAINTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Constraints = _reflection.GeneratedProtocolMessageType('Constraints', (_message.Message,), {
  'DESCRIPTOR' : _CONSTRAINTS,
  '__module__' : 'systemathics.apis.type.shared.v1.constraints_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.type.shared.v1.Constraints)
  })
_sym_db.RegisterMessage(Constraints)


# @@protoc_insertion_point(module_scope)
