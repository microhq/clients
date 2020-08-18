# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: config/source/service.proto for package ''

require 'grpc'
require 'config/source/service_pb'

module Config
  class Service

    include GRPC::GenericService

    self.marshal_class_method = :encode
    self.unmarshal_class_method = :decode
    self.service_name = 'Config'

    rpc :Create, ::CreateRequest, ::CreateResponse
    rpc :Update, ::UpdateRequest, ::UpdateResponse
    rpc :Delete, ::DeleteRequest, ::DeleteResponse
    rpc :List, ::ListRequest, ::ListResponse
    rpc :Read, ::ReadRequest, ::ReadResponse
    rpc :Watch, ::WatchRequest, stream(::WatchResponse)
  end

  Stub = Service.rpc_stub_class
end
