# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: store/store.proto for package 'go.micro.store'

require 'grpc'
require 'store/store_pb'

module Go
  module Micro
    module Store
      module Store
        class Service

          include GRPC::GenericService

          self.marshal_class_method = :encode
          self.unmarshal_class_method = :decode
          self.service_name = 'go.micro.store.Store'

          rpc :List, ListRequest, stream(ListResponse)
          rpc :Read, ReadRequest, ReadResponse
          rpc :Write, WriteRequest, WriteResponse
          rpc :Delete, DeleteRequest, DeleteResponse
        end

        Stub = Service.rpc_stub_class
      end
    end
  end
end
