# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth/auth.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth/auth.proto',
  package='go.micro.auth',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x61uth/auth.proto\x12\rgo.micro.auth\"\xdf\x01\n\x05Token\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07\x63reated\x18\x03 \x01(\x03\x12\x0e\n\x06\x65xpiry\x18\x04 \x01(\x03\x12\x0f\n\x07subject\x18\x05 \x01(\t\x12\r\n\x05roles\x18\x06 \x03(\t\x12\x34\n\x08metadata\x18\x07 \x03(\x0b\x32\".go.micro.auth.Token.MetadataEntry\x12\x11\n\tnamespace\x18\x08 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc6\x01\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\t\x12$\n\x06secret\x18\x02 \x01(\x0b\x32\x14.go.micro.auth.Token\x12\r\n\x05roles\x18\x03 \x03(\t\x12\x36\n\x08metadata\x18\x04 \x03(\x0b\x32$.go.micro.auth.Account.MetadataEntry\x12\x11\n\tnamespace\x18\x05 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"8\n\x08Resource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x03 \x01(\t\"\xc7\x01\n\x0fGenerateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05roles\x18\x02 \x03(\t\x12>\n\x08metadata\x18\x03 \x03(\x0b\x32,.go.micro.auth.GenerateRequest.MetadataEntry\x12\x15\n\rsecret_expiry\x18\x04 \x01(\x03\x12\x11\n\tnamespace\x18\x05 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\";\n\x10GenerateResponse\x12\'\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x16.go.micro.auth.Account\"G\n\x0cGrantRequest\x12\x0c\n\x04role\x18\x01 \x01(\t\x12)\n\x08resource\x18\x02 \x01(\x0b\x32\x17.go.micro.auth.Resource\"\x0f\n\rGrantResponse\"H\n\rRevokeRequest\x12\x0c\n\x04role\x18\x01 \x01(\t\x12)\n\x08resource\x18\x02 \x01(\x0b\x32\x17.go.micro.auth.Resource\"\x10\n\x0eRevokeResponse\"\x1f\n\x0eInspectRequest\x12\r\n\x05token\x18\x01 \x01(\t\":\n\x0fInspectResponse\x12\'\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x16.go.micro.auth.Account\"6\n\x0eRefreshRequest\x12\x0e\n\x06secret\x18\x01 \x01(\t\x12\x14\n\x0ctoken_expiry\x18\x02 \x01(\x03\"6\n\x0fRefreshResponse\x12#\n\x05token\x18\x01 \x01(\x0b\x32\x14.go.micro.auth.Token2\xed\x01\n\x04\x41uth\x12M\n\x08Generate\x12\x1e.go.micro.auth.GenerateRequest\x1a\x1f.go.micro.auth.GenerateResponse\"\x00\x12J\n\x07Inspect\x12\x1d.go.micro.auth.InspectRequest\x1a\x1e.go.micro.auth.InspectResponse\"\x00\x12J\n\x07Refresh\x12\x1d.go.micro.auth.RefreshRequest\x1a\x1e.go.micro.auth.RefreshResponse\"\x00\x42\x0bZ\tauth;authb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TOKEN_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='go.micro.auth.Token.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='go.micro.auth.Token.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='go.micro.auth.Token.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=258,
)

_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='go.micro.auth.Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='go.micro.auth.Token.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='go.micro.auth.Token.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='go.micro.auth.Token.created', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiry', full_name='go.micro.auth.Token.expiry', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subject', full_name='go.micro.auth.Token.subject', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roles', full_name='go.micro.auth.Token.roles', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='go.micro.auth.Token.metadata', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='go.micro.auth.Token.namespace', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TOKEN_METADATAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=258,
)


_ACCOUNT_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='go.micro.auth.Account.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='go.micro.auth.Account.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='go.micro.auth.Account.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=258,
)

_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='go.micro.auth.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='go.micro.auth.Account.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secret', full_name='go.micro.auth.Account.secret', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roles', full_name='go.micro.auth.Account.roles', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='go.micro.auth.Account.metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='go.micro.auth.Account.namespace', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ACCOUNT_METADATAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=459,
)


_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='go.micro.auth.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='go.micro.auth.Resource.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='go.micro.auth.Resource.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='go.micro.auth.Resource.endpoint', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=517,
)


_GENERATEREQUEST_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='go.micro.auth.GenerateRequest.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='go.micro.auth.GenerateRequest.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='go.micro.auth.GenerateRequest.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=258,
)

_GENERATEREQUEST = _descriptor.Descriptor(
  name='GenerateRequest',
  full_name='go.micro.auth.GenerateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='go.micro.auth.GenerateRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roles', full_name='go.micro.auth.GenerateRequest.roles', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='go.micro.auth.GenerateRequest.metadata', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secret_expiry', full_name='go.micro.auth.GenerateRequest.secret_expiry', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='go.micro.auth.GenerateRequest.namespace', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GENERATEREQUEST_METADATAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=520,
  serialized_end=719,
)


_GENERATERESPONSE = _descriptor.Descriptor(
  name='GenerateResponse',
  full_name='go.micro.auth.GenerateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='go.micro.auth.GenerateResponse.account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=721,
  serialized_end=780,
)


_GRANTREQUEST = _descriptor.Descriptor(
  name='GrantRequest',
  full_name='go.micro.auth.GrantRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='go.micro.auth.GrantRequest.role', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='go.micro.auth.GrantRequest.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=782,
  serialized_end=853,
)


_GRANTRESPONSE = _descriptor.Descriptor(
  name='GrantResponse',
  full_name='go.micro.auth.GrantResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=855,
  serialized_end=870,
)


_REVOKEREQUEST = _descriptor.Descriptor(
  name='RevokeRequest',
  full_name='go.micro.auth.RevokeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='go.micro.auth.RevokeRequest.role', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='go.micro.auth.RevokeRequest.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=872,
  serialized_end=944,
)


_REVOKERESPONSE = _descriptor.Descriptor(
  name='RevokeResponse',
  full_name='go.micro.auth.RevokeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=946,
  serialized_end=962,
)


_INSPECTREQUEST = _descriptor.Descriptor(
  name='InspectRequest',
  full_name='go.micro.auth.InspectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='go.micro.auth.InspectRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=964,
  serialized_end=995,
)


_INSPECTRESPONSE = _descriptor.Descriptor(
  name='InspectResponse',
  full_name='go.micro.auth.InspectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='go.micro.auth.InspectResponse.account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=997,
  serialized_end=1055,
)


_REFRESHREQUEST = _descriptor.Descriptor(
  name='RefreshRequest',
  full_name='go.micro.auth.RefreshRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret', full_name='go.micro.auth.RefreshRequest.secret', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token_expiry', full_name='go.micro.auth.RefreshRequest.token_expiry', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1057,
  serialized_end=1111,
)


_REFRESHRESPONSE = _descriptor.Descriptor(
  name='RefreshResponse',
  full_name='go.micro.auth.RefreshResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='go.micro.auth.RefreshResponse.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1113,
  serialized_end=1167,
)

_TOKEN_METADATAENTRY.containing_type = _TOKEN
_TOKEN.fields_by_name['metadata'].message_type = _TOKEN_METADATAENTRY
_ACCOUNT_METADATAENTRY.containing_type = _ACCOUNT
_ACCOUNT.fields_by_name['secret'].message_type = _TOKEN
_ACCOUNT.fields_by_name['metadata'].message_type = _ACCOUNT_METADATAENTRY
_GENERATEREQUEST_METADATAENTRY.containing_type = _GENERATEREQUEST
_GENERATEREQUEST.fields_by_name['metadata'].message_type = _GENERATEREQUEST_METADATAENTRY
_GENERATERESPONSE.fields_by_name['account'].message_type = _ACCOUNT
_GRANTREQUEST.fields_by_name['resource'].message_type = _RESOURCE
_REVOKEREQUEST.fields_by_name['resource'].message_type = _RESOURCE
_INSPECTRESPONSE.fields_by_name['account'].message_type = _ACCOUNT
_REFRESHRESPONSE.fields_by_name['token'].message_type = _TOKEN
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
DESCRIPTOR.message_types_by_name['GenerateRequest'] = _GENERATEREQUEST
DESCRIPTOR.message_types_by_name['GenerateResponse'] = _GENERATERESPONSE
DESCRIPTOR.message_types_by_name['GrantRequest'] = _GRANTREQUEST
DESCRIPTOR.message_types_by_name['GrantResponse'] = _GRANTRESPONSE
DESCRIPTOR.message_types_by_name['RevokeRequest'] = _REVOKEREQUEST
DESCRIPTOR.message_types_by_name['RevokeResponse'] = _REVOKERESPONSE
DESCRIPTOR.message_types_by_name['InspectRequest'] = _INSPECTREQUEST
DESCRIPTOR.message_types_by_name['InspectResponse'] = _INSPECTRESPONSE
DESCRIPTOR.message_types_by_name['RefreshRequest'] = _REFRESHREQUEST
DESCRIPTOR.message_types_by_name['RefreshResponse'] = _REFRESHRESPONSE

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _TOKEN_METADATAENTRY,
    __module__ = 'auth.auth_pb2'
    # @@protoc_insertion_point(class_scope:go.micro.auth.Token.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _TOKEN,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.Token)
  ))
_sym_db.RegisterMessage(Token)
_sym_db.RegisterMessage(Token.MetadataEntry)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _ACCOUNT_METADATAENTRY,
    __module__ = 'auth.auth_pb2'
    # @@protoc_insertion_point(class_scope:go.micro.auth.Account.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _ACCOUNT,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.Account)
  ))
_sym_db.RegisterMessage(Account)
_sym_db.RegisterMessage(Account.MetadataEntry)

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCE,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.Resource)
  ))
_sym_db.RegisterMessage(Resource)

GenerateRequest = _reflection.GeneratedProtocolMessageType('GenerateRequest', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _GENERATEREQUEST_METADATAENTRY,
    __module__ = 'auth.auth_pb2'
    # @@protoc_insertion_point(class_scope:go.micro.auth.GenerateRequest.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _GENERATEREQUEST,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.GenerateRequest)
  ))
_sym_db.RegisterMessage(GenerateRequest)
_sym_db.RegisterMessage(GenerateRequest.MetadataEntry)

GenerateResponse = _reflection.GeneratedProtocolMessageType('GenerateResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERATERESPONSE,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.GenerateResponse)
  ))
_sym_db.RegisterMessage(GenerateResponse)

GrantRequest = _reflection.GeneratedProtocolMessageType('GrantRequest', (_message.Message,), dict(
  DESCRIPTOR = _GRANTREQUEST,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.GrantRequest)
  ))
_sym_db.RegisterMessage(GrantRequest)

GrantResponse = _reflection.GeneratedProtocolMessageType('GrantResponse', (_message.Message,), dict(
  DESCRIPTOR = _GRANTRESPONSE,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.GrantResponse)
  ))
_sym_db.RegisterMessage(GrantResponse)

RevokeRequest = _reflection.GeneratedProtocolMessageType('RevokeRequest', (_message.Message,), dict(
  DESCRIPTOR = _REVOKEREQUEST,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.RevokeRequest)
  ))
_sym_db.RegisterMessage(RevokeRequest)

RevokeResponse = _reflection.GeneratedProtocolMessageType('RevokeResponse', (_message.Message,), dict(
  DESCRIPTOR = _REVOKERESPONSE,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.RevokeResponse)
  ))
_sym_db.RegisterMessage(RevokeResponse)

InspectRequest = _reflection.GeneratedProtocolMessageType('InspectRequest', (_message.Message,), dict(
  DESCRIPTOR = _INSPECTREQUEST,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.InspectRequest)
  ))
_sym_db.RegisterMessage(InspectRequest)

InspectResponse = _reflection.GeneratedProtocolMessageType('InspectResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSPECTRESPONSE,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.InspectResponse)
  ))
_sym_db.RegisterMessage(InspectResponse)

RefreshRequest = _reflection.GeneratedProtocolMessageType('RefreshRequest', (_message.Message,), dict(
  DESCRIPTOR = _REFRESHREQUEST,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.RefreshRequest)
  ))
_sym_db.RegisterMessage(RefreshRequest)

RefreshResponse = _reflection.GeneratedProtocolMessageType('RefreshResponse', (_message.Message,), dict(
  DESCRIPTOR = _REFRESHRESPONSE,
  __module__ = 'auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.RefreshResponse)
  ))
_sym_db.RegisterMessage(RefreshResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\tauth;auth'))
_TOKEN_METADATAENTRY.has_options = True
_TOKEN_METADATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_ACCOUNT_METADATAENTRY.has_options = True
_ACCOUNT_METADATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_GENERATEREQUEST_METADATAENTRY.has_options = True
_GENERATEREQUEST_METADATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
