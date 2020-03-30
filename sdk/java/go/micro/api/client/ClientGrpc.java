package go.micro.api.client;

import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ClientCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ClientCalls.asyncClientStreamingCall;
import static io.grpc.stub.ClientCalls.asyncServerStreamingCall;
import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.stub.ServerCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ServerCalls.asyncClientStreamingCall;
import static io.grpc.stub.ServerCalls.asyncServerStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;

/**
 * <pre>
 * Client is the micro client api
 * </pre>
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.28.0)",
    comments = "Source: client/client.proto")
public final class ClientGrpc {

  private ClientGrpc() {}

  public static final String SERVICE_NAME = "go.micro.api.client.Client";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<go.micro.api.client.ClientOuterClass.Request,
      go.micro.api.client.ClientOuterClass.Response> getCallMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "Call",
      requestType = go.micro.api.client.ClientOuterClass.Request.class,
      responseType = go.micro.api.client.ClientOuterClass.Response.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<go.micro.api.client.ClientOuterClass.Request,
      go.micro.api.client.ClientOuterClass.Response> getCallMethod() {
    io.grpc.MethodDescriptor<go.micro.api.client.ClientOuterClass.Request, go.micro.api.client.ClientOuterClass.Response> getCallMethod;
    if ((getCallMethod = ClientGrpc.getCallMethod) == null) {
      synchronized (ClientGrpc.class) {
        if ((getCallMethod = ClientGrpc.getCallMethod) == null) {
          ClientGrpc.getCallMethod = getCallMethod =
              io.grpc.MethodDescriptor.<go.micro.api.client.ClientOuterClass.Request, go.micro.api.client.ClientOuterClass.Response>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "Call"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  go.micro.api.client.ClientOuterClass.Request.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  go.micro.api.client.ClientOuterClass.Response.getDefaultInstance()))
              .setSchemaDescriptor(new ClientMethodDescriptorSupplier("Call"))
              .build();
        }
      }
    }
    return getCallMethod;
  }

  private static volatile io.grpc.MethodDescriptor<go.micro.api.client.ClientOuterClass.Request,
      go.micro.api.client.ClientOuterClass.Response> getStreamMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "Stream",
      requestType = go.micro.api.client.ClientOuterClass.Request.class,
      responseType = go.micro.api.client.ClientOuterClass.Response.class,
      methodType = io.grpc.MethodDescriptor.MethodType.BIDI_STREAMING)
  public static io.grpc.MethodDescriptor<go.micro.api.client.ClientOuterClass.Request,
      go.micro.api.client.ClientOuterClass.Response> getStreamMethod() {
    io.grpc.MethodDescriptor<go.micro.api.client.ClientOuterClass.Request, go.micro.api.client.ClientOuterClass.Response> getStreamMethod;
    if ((getStreamMethod = ClientGrpc.getStreamMethod) == null) {
      synchronized (ClientGrpc.class) {
        if ((getStreamMethod = ClientGrpc.getStreamMethod) == null) {
          ClientGrpc.getStreamMethod = getStreamMethod =
              io.grpc.MethodDescriptor.<go.micro.api.client.ClientOuterClass.Request, go.micro.api.client.ClientOuterClass.Response>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.BIDI_STREAMING)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "Stream"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  go.micro.api.client.ClientOuterClass.Request.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  go.micro.api.client.ClientOuterClass.Response.getDefaultInstance()))
              .setSchemaDescriptor(new ClientMethodDescriptorSupplier("Stream"))
              .build();
        }
      }
    }
    return getStreamMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static ClientStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ClientStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ClientStub>() {
        @java.lang.Override
        public ClientStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ClientStub(channel, callOptions);
        }
      };
    return ClientStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static ClientBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ClientBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ClientBlockingStub>() {
        @java.lang.Override
        public ClientBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ClientBlockingStub(channel, callOptions);
        }
      };
    return ClientBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static ClientFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<ClientFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<ClientFutureStub>() {
        @java.lang.Override
        public ClientFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new ClientFutureStub(channel, callOptions);
        }
      };
    return ClientFutureStub.newStub(factory, channel);
  }

  /**
   * <pre>
   * Client is the micro client api
   * </pre>
   */
  public static abstract class ClientImplBase implements io.grpc.BindableService {

    /**
     * <pre>
     * Call allows a single request to be made
     * </pre>
     */
    public void call(go.micro.api.client.ClientOuterClass.Request request,
        io.grpc.stub.StreamObserver<go.micro.api.client.ClientOuterClass.Response> responseObserver) {
      asyncUnimplementedUnaryCall(getCallMethod(), responseObserver);
    }

    /**
     * <pre>
     * Stream is a bidirectional stream
     * </pre>
     */
    public io.grpc.stub.StreamObserver<go.micro.api.client.ClientOuterClass.Request> stream(
        io.grpc.stub.StreamObserver<go.micro.api.client.ClientOuterClass.Response> responseObserver) {
      return asyncUnimplementedStreamingCall(getStreamMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getCallMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                go.micro.api.client.ClientOuterClass.Request,
                go.micro.api.client.ClientOuterClass.Response>(
                  this, METHODID_CALL)))
          .addMethod(
            getStreamMethod(),
            asyncBidiStreamingCall(
              new MethodHandlers<
                go.micro.api.client.ClientOuterClass.Request,
                go.micro.api.client.ClientOuterClass.Response>(
                  this, METHODID_STREAM)))
          .build();
    }
  }

  /**
   * <pre>
   * Client is the micro client api
   * </pre>
   */
  public static final class ClientStub extends io.grpc.stub.AbstractAsyncStub<ClientStub> {
    private ClientStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ClientStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ClientStub(channel, callOptions);
    }

    /**
     * <pre>
     * Call allows a single request to be made
     * </pre>
     */
    public void call(go.micro.api.client.ClientOuterClass.Request request,
        io.grpc.stub.StreamObserver<go.micro.api.client.ClientOuterClass.Response> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getCallMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Stream is a bidirectional stream
     * </pre>
     */
    public io.grpc.stub.StreamObserver<go.micro.api.client.ClientOuterClass.Request> stream(
        io.grpc.stub.StreamObserver<go.micro.api.client.ClientOuterClass.Response> responseObserver) {
      return asyncBidiStreamingCall(
          getChannel().newCall(getStreamMethod(), getCallOptions()), responseObserver);
    }
  }

  /**
   * <pre>
   * Client is the micro client api
   * </pre>
   */
  public static final class ClientBlockingStub extends io.grpc.stub.AbstractBlockingStub<ClientBlockingStub> {
    private ClientBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ClientBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ClientBlockingStub(channel, callOptions);
    }

    /**
     * <pre>
     * Call allows a single request to be made
     * </pre>
     */
    public go.micro.api.client.ClientOuterClass.Response call(go.micro.api.client.ClientOuterClass.Request request) {
      return blockingUnaryCall(
          getChannel(), getCallMethod(), getCallOptions(), request);
    }
  }

  /**
   * <pre>
   * Client is the micro client api
   * </pre>
   */
  public static final class ClientFutureStub extends io.grpc.stub.AbstractFutureStub<ClientFutureStub> {
    private ClientFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected ClientFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new ClientFutureStub(channel, callOptions);
    }

    /**
     * <pre>
     * Call allows a single request to be made
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<go.micro.api.client.ClientOuterClass.Response> call(
        go.micro.api.client.ClientOuterClass.Request request) {
      return futureUnaryCall(
          getChannel().newCall(getCallMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_CALL = 0;
  private static final int METHODID_STREAM = 1;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final ClientImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(ClientImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_CALL:
          serviceImpl.call((go.micro.api.client.ClientOuterClass.Request) request,
              (io.grpc.stub.StreamObserver<go.micro.api.client.ClientOuterClass.Response>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_STREAM:
          return (io.grpc.stub.StreamObserver<Req>) serviceImpl.stream(
              (io.grpc.stub.StreamObserver<go.micro.api.client.ClientOuterClass.Response>) responseObserver);
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class ClientBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    ClientBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return go.micro.api.client.ClientOuterClass.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("Client");
    }
  }

  private static final class ClientFileDescriptorSupplier
      extends ClientBaseDescriptorSupplier {
    ClientFileDescriptorSupplier() {}
  }

  private static final class ClientMethodDescriptorSupplier
      extends ClientBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    ClientMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (ClientGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new ClientFileDescriptorSupplier())
              .addMethod(getCallMethod())
              .addMethod(getStreamMethod())
              .build();
        }
      }
    }
    return result;
  }
}
