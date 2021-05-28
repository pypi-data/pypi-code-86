# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick/v1/tick_book.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2
from systemathics.apis.type.shared.v1 import mappings_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_mappings__pb2
from systemathics.apis.type.shared.v1 import level_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_level__pb2
from systemathics.apis.type.shared.v1 import market_book_updates_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_market__book__updates__pb2
from systemathics.apis.type.shared.v1 import market_fields_updates_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_market__fields__updates__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import keys_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_keys__pb2
from systemathics.apis.type.shared.v1 import book_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_book__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='systemathics/apis/services/tick/v1/tick_book.proto',
  package='systemathics.apis.services.tick.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2systemathics/apis/services/tick/v1/tick_book.proto\x12\"systemathics.apis.services.tick.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a/systemathics/apis/type/shared/v1/mappings.proto\x1a,systemathics/apis/type/shared/v1/level.proto\x1a:systemathics/apis/type/shared/v1/market_book_updates.proto\x1a<systemathics/apis/type/shared/v1/market_fields_updates.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a+systemathics/apis/type/shared/v1/keys.proto\x1a+systemathics/apis/type/shared/v1/book.proto\"\x98\x01\n\x0fTickBookRequest\x12\x41\n\x0bidentifiers\x18\x01 \x03(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x42\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.Constraints\"\x96\x01\n\x10TickBookResponse\x12<\n\x05limit\x18\x01 \x01(\x0b\x32+.systemathics.apis.type.shared.v1.BookLimitH\x00\x12\x39\n\x07mapping\x18\x02 \x01(\x0b\x32&.systemathics.apis.type.shared.v1.KeysH\x00\x42\t\n\x07payload2\x8a\x01\n\x0fTickBookService\x12w\n\x08TickBook\x12\x33.systemathics.apis.services.tick.v1.TickBookRequest\x1a\x34.systemathics.apis.services.tick.v1.TickBookResponse0\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_mappings__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_level__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_market__book__updates__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_market__fields__updates__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_keys__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_book__pb2.DESCRIPTOR,])




_TICKBOOKREQUEST = _descriptor.Descriptor(
  name='TickBookRequest',
  full_name='systemathics.apis.services.tick.v1.TickBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='systemathics.apis.services.tick.v1.TickBookRequest.identifiers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='systemathics.apis.services.tick.v1.TickBookRequest.constraints', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=534,
  serialized_end=686,
)


_TICKBOOKRESPONSE = _descriptor.Descriptor(
  name='TickBookResponse',
  full_name='systemathics.apis.services.tick.v1.TickBookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='systemathics.apis.services.tick.v1.TickBookResponse.limit', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mapping', full_name='systemathics.apis.services.tick.v1.TickBookResponse.mapping', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='systemathics.apis.services.tick.v1.TickBookResponse.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=689,
  serialized_end=839,
)

_TICKBOOKREQUEST.fields_by_name['identifiers'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2._IDENTIFIER
_TICKBOOKREQUEST.fields_by_name['constraints'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2._CONSTRAINTS
_TICKBOOKRESPONSE.fields_by_name['limit'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_book__pb2._BOOKLIMIT
_TICKBOOKRESPONSE.fields_by_name['mapping'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_keys__pb2._KEYS
_TICKBOOKRESPONSE.oneofs_by_name['payload'].fields.append(
  _TICKBOOKRESPONSE.fields_by_name['limit'])
_TICKBOOKRESPONSE.fields_by_name['limit'].containing_oneof = _TICKBOOKRESPONSE.oneofs_by_name['payload']
_TICKBOOKRESPONSE.oneofs_by_name['payload'].fields.append(
  _TICKBOOKRESPONSE.fields_by_name['mapping'])
_TICKBOOKRESPONSE.fields_by_name['mapping'].containing_oneof = _TICKBOOKRESPONSE.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['TickBookRequest'] = _TICKBOOKREQUEST
DESCRIPTOR.message_types_by_name['TickBookResponse'] = _TICKBOOKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TickBookRequest = _reflection.GeneratedProtocolMessageType('TickBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _TICKBOOKREQUEST,
  '__module__' : 'systemathics.apis.services.tick.v1.tick_book_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.tick.v1.TickBookRequest)
  })
_sym_db.RegisterMessage(TickBookRequest)

TickBookResponse = _reflection.GeneratedProtocolMessageType('TickBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _TICKBOOKRESPONSE,
  '__module__' : 'systemathics.apis.services.tick.v1.tick_book_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.tick.v1.TickBookResponse)
  })
_sym_db.RegisterMessage(TickBookResponse)



_TICKBOOKSERVICE = _descriptor.ServiceDescriptor(
  name='TickBookService',
  full_name='systemathics.apis.services.tick.v1.TickBookService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=842,
  serialized_end=980,
  methods=[
  _descriptor.MethodDescriptor(
    name='TickBook',
    full_name='systemathics.apis.services.tick.v1.TickBookService.TickBook',
    index=0,
    containing_service=None,
    input_type=_TICKBOOKREQUEST,
    output_type=_TICKBOOKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TICKBOOKSERVICE)

DESCRIPTOR.services_by_name['TickBookService'] = _TICKBOOKSERVICE

# @@protoc_insertion_point(module_scope)
