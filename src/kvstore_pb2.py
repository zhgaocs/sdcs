# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kvstore.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rkvstore.proto\x1a\x19google/protobuf/any.proto\">\n\nSetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"\x1e\n\x0bSetResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"2\n\x0bGetResponse\x12#\n\x05value\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"\x1c\n\rRemoveRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"!\n\x0eRemoveResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32~\n\x07KVStore\x12\"\n\x03Set\x12\x0b.SetRequest\x1a\x0c.SetResponse\"\x00\x12\"\n\x03Get\x12\x0b.GetRequest\x1a\x0c.GetResponse\"\x00\x12+\n\x06Remove\x12\x0e.RemoveRequest\x1a\x0f.RemoveResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kvstore_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SETREQUEST']._serialized_start=44
  _globals['_SETREQUEST']._serialized_end=106
  _globals['_SETRESPONSE']._serialized_start=108
  _globals['_SETRESPONSE']._serialized_end=138
  _globals['_GETREQUEST']._serialized_start=140
  _globals['_GETREQUEST']._serialized_end=165
  _globals['_GETRESPONSE']._serialized_start=167
  _globals['_GETRESPONSE']._serialized_end=217
  _globals['_REMOVEREQUEST']._serialized_start=219
  _globals['_REMOVEREQUEST']._serialized_end=247
  _globals['_REMOVERESPONSE']._serialized_start=249
  _globals['_REMOVERESPONSE']._serialized_end=282
  _globals['_KVSTORE']._serialized_start=284
  _globals['_KVSTORE']._serialized_end=410
# @@protoc_insertion_point(module_scope)
