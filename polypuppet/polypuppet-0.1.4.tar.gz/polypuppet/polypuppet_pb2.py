# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: polypuppet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='polypuppet.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10polypuppet.proto\x1a\x1bgoogle/protobuf/empty.proto\"5\n\x02PC\x12\x0c\n\x04uuid\x18\x01 \x01(\x04\x12\x10\n\x08platform\x18\x02 \x01(\t\x12\x0f\n\x07release\x18\x03 \x01(\t\"*\n\x04User\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"N\n\x08\x41udience\x12\x0f\n\x02pc\x18\x01 \x01(\x0b\x32\x03.PC\x12\x10\n\x08\x62uilding\x18\x02 \x01(\r\x12\x10\n\x08\x61udience\x18\x03 \x01(\r\x12\r\n\x05token\x18\x04 \x01(\t\"}\n\x07Profile\x12\x13\n\x04role\x18\x01 \x01(\x0e\x32\x05.Role\x12\x10\n\x08\x63\x65rtname\x18\x02 \x01(\t\x12\x0c\n\x04\x66low\x18\x03 \x01(\t\x12\r\n\x05group\x18\x04 \x01(\t\x12\x10\n\x08\x62uilding\x18\x05 \x01(\r\x12\x10\n\x08\x61udience\x18\x06 \x01(\r\x12\n\n\x02ok\x18\x07 \x01(\x08\"\x1c\n\x08\x43\x65rtname\x12\x10\n\x08\x63\x65rtname\x18\x01 \x01(\t\"\x16\n\x08\x41utosign\x12\n\n\x02ok\x18\x01 \x01(\x08\"5\n\x05Token\x12\x1d\n\x07taction\x18\x01 \x01(\x0e\x32\x0c.TokenAction\x12\r\n\x05token\x18\x02 \x01(\t*,\n\x04Role\x12\x0c\n\x08\x41UDIENCE\x10\x00\x12\x0b\n\x07STUDENT\x10\x01\x12\t\n\x05OTHER\x10\x02**\n\x0bTokenAction\x12\x07\n\x03GET\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\t\n\x05\x43LEAR\x10\x02\x32\\\n\x10RemoteConnection\x12\x1f\n\nlogin_user\x12\x05.User\x1a\x08.Profile\"\x00\x12\'\n\x0elogin_audience\x12\t.Audience\x1a\x08.Profile\"\x00\x32\x91\x01\n\x0fLocalConnection\x12 \n\x0cmanage_token\x12\x06.Token\x1a\x06.Token\"\x00\x12\"\n\x08\x61utosign\x12\t.Certname\x1a\t.Autosign\"\x00\x12\x38\n\x04stop\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='Role',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUDIENCE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STUDENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=464,
  serialized_end=508,
)
_sym_db.RegisterEnumDescriptor(_ROLE)

Role = enum_type_wrapper.EnumTypeWrapper(_ROLE)
_TOKENACTION = _descriptor.EnumDescriptor(
  name='TokenAction',
  full_name='TokenAction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GET', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLEAR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=510,
  serialized_end=552,
)
_sym_db.RegisterEnumDescriptor(_TOKENACTION)

TokenAction = enum_type_wrapper.EnumTypeWrapper(_TOKENACTION)
AUDIENCE = 0
STUDENT = 1
OTHER = 2
GET = 0
NEW = 1
CLEAR = 2



_PC = _descriptor.Descriptor(
  name='PC',
  full_name='PC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='PC.uuid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='platform', full_name='PC.platform', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='release', full_name='PC.release', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=49,
  serialized_end=102,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='User.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='User.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=104,
  serialized_end=146,
)


_AUDIENCE = _descriptor.Descriptor(
  name='Audience',
  full_name='Audience',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pc', full_name='Audience.pc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='building', full_name='Audience.building', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audience', full_name='Audience.audience', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='Audience.token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=148,
  serialized_end=226,
)


_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='Profile.role', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='certname', full_name='Profile.certname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flow', full_name='Profile.flow', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group', full_name='Profile.group', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='building', full_name='Profile.building', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audience', full_name='Profile.audience', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ok', full_name='Profile.ok', index=6,
      number=7, type=8, cpp_type=7, label=1,
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
  serialized_start=228,
  serialized_end=353,
)


_CERTNAME = _descriptor.Descriptor(
  name='Certname',
  full_name='Certname',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='certname', full_name='Certname.certname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=355,
  serialized_end=383,
)


_AUTOSIGN = _descriptor.Descriptor(
  name='Autosign',
  full_name='Autosign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ok', full_name='Autosign.ok', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=385,
  serialized_end=407,
)


_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='taction', full_name='Token.taction', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='Token.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_end=462,
)

_AUDIENCE.fields_by_name['pc'].message_type = _PC
_PROFILE.fields_by_name['role'].enum_type = _ROLE
_TOKEN.fields_by_name['taction'].enum_type = _TOKENACTION
DESCRIPTOR.message_types_by_name['PC'] = _PC
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Audience'] = _AUDIENCE
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.message_types_by_name['Certname'] = _CERTNAME
DESCRIPTOR.message_types_by_name['Autosign'] = _AUTOSIGN
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.enum_types_by_name['Role'] = _ROLE
DESCRIPTOR.enum_types_by_name['TokenAction'] = _TOKENACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PC = _reflection.GeneratedProtocolMessageType('PC', (_message.Message,), {
  'DESCRIPTOR' : _PC,
  '__module__' : 'polypuppet_pb2'
  # @@protoc_insertion_point(class_scope:PC)
  })
_sym_db.RegisterMessage(PC)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'polypuppet_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)

Audience = _reflection.GeneratedProtocolMessageType('Audience', (_message.Message,), {
  'DESCRIPTOR' : _AUDIENCE,
  '__module__' : 'polypuppet_pb2'
  # @@protoc_insertion_point(class_scope:Audience)
  })
_sym_db.RegisterMessage(Audience)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), {
  'DESCRIPTOR' : _PROFILE,
  '__module__' : 'polypuppet_pb2'
  # @@protoc_insertion_point(class_scope:Profile)
  })
_sym_db.RegisterMessage(Profile)

Certname = _reflection.GeneratedProtocolMessageType('Certname', (_message.Message,), {
  'DESCRIPTOR' : _CERTNAME,
  '__module__' : 'polypuppet_pb2'
  # @@protoc_insertion_point(class_scope:Certname)
  })
_sym_db.RegisterMessage(Certname)

Autosign = _reflection.GeneratedProtocolMessageType('Autosign', (_message.Message,), {
  'DESCRIPTOR' : _AUTOSIGN,
  '__module__' : 'polypuppet_pb2'
  # @@protoc_insertion_point(class_scope:Autosign)
  })
_sym_db.RegisterMessage(Autosign)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'polypuppet_pb2'
  # @@protoc_insertion_point(class_scope:Token)
  })
_sym_db.RegisterMessage(Token)



_REMOTECONNECTION = _descriptor.ServiceDescriptor(
  name='RemoteConnection',
  full_name='RemoteConnection',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=554,
  serialized_end=646,
  methods=[
  _descriptor.MethodDescriptor(
    name='login_user',
    full_name='RemoteConnection.login_user',
    index=0,
    containing_service=None,
    input_type=_USER,
    output_type=_PROFILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='login_audience',
    full_name='RemoteConnection.login_audience',
    index=1,
    containing_service=None,
    input_type=_AUDIENCE,
    output_type=_PROFILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REMOTECONNECTION)

DESCRIPTOR.services_by_name['RemoteConnection'] = _REMOTECONNECTION


_LOCALCONNECTION = _descriptor.ServiceDescriptor(
  name='LocalConnection',
  full_name='LocalConnection',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=649,
  serialized_end=794,
  methods=[
  _descriptor.MethodDescriptor(
    name='manage_token',
    full_name='LocalConnection.manage_token',
    index=0,
    containing_service=None,
    input_type=_TOKEN,
    output_type=_TOKEN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='autosign',
    full_name='LocalConnection.autosign',
    index=1,
    containing_service=None,
    input_type=_CERTNAME,
    output_type=_AUTOSIGN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stop',
    full_name='LocalConnection.stop',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCALCONNECTION)

DESCRIPTOR.services_by_name['LocalConnection'] = _LOCALCONNECTION

# @@protoc_insertion_point(module_scope)
