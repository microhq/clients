# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: router/router.proto for package 'go.micro.router'

require 'grpc'
require 'router/router_pb'

module Go
  module Micro
    module Router
      module Router
        # Router service is used by the proxy to lookup routes
        class Service

          include GRPC::GenericService

          self.marshal_class_method = :encode
          self.unmarshal_class_method = :decode
          self.service_name = 'go.micro.router.Router'

          rpc :Lookup, LookupRequest, LookupResponse
          rpc :Watch, WatchRequest, stream(Event)
          rpc :Advertise, Request, stream(Advert)
          rpc :Solicit, Request, Response
          rpc :Process, Advert, ProcessResponse
          rpc :Status, Request, StatusResponse
        end

        Stub = Service.rpc_stub_class
      end
      module Table
        class Service

          include GRPC::GenericService

          self.marshal_class_method = :encode
          self.unmarshal_class_method = :decode
          self.service_name = 'go.micro.router.Table'

          rpc :Create, Route, CreateResponse
          rpc :Delete, Route, DeleteResponse
          rpc :Update, Route, UpdateResponse
          rpc :List, Request, ListResponse
          rpc :Query, QueryRequest, QueryResponse
        end

        Stub = Service.rpc_stub_class
      end
    end
  end
end
