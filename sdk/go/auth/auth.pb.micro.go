// Code generated by protoc-gen-micro. DO NOT EDIT.
// source: auth/auth.proto

package auth

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

import (
	context "context"
	client "github.com/micro/go-micro/v2/client"
	server "github.com/micro/go-micro/v2/server"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ client.Option
var _ server.Option

// Client API for Auth service

type AuthService interface {
	Generate(ctx context.Context, in *GenerateRequest, opts ...client.CallOption) (*GenerateResponse, error)
	Inspect(ctx context.Context, in *InspectRequest, opts ...client.CallOption) (*InspectResponse, error)
	Refresh(ctx context.Context, in *RefreshRequest, opts ...client.CallOption) (*RefreshResponse, error)
}

type authService struct {
	c    client.Client
	name string
}

func NewAuthService(name string, c client.Client) AuthService {
	return &authService{
		c:    c,
		name: name,
	}
}

func (c *authService) Generate(ctx context.Context, in *GenerateRequest, opts ...client.CallOption) (*GenerateResponse, error) {
	req := c.c.NewRequest(c.name, "Auth.Generate", in)
	out := new(GenerateResponse)
	err := c.c.Call(ctx, req, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *authService) Inspect(ctx context.Context, in *InspectRequest, opts ...client.CallOption) (*InspectResponse, error) {
	req := c.c.NewRequest(c.name, "Auth.Inspect", in)
	out := new(InspectResponse)
	err := c.c.Call(ctx, req, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *authService) Refresh(ctx context.Context, in *RefreshRequest, opts ...client.CallOption) (*RefreshResponse, error) {
	req := c.c.NewRequest(c.name, "Auth.Refresh", in)
	out := new(RefreshResponse)
	err := c.c.Call(ctx, req, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// Server API for Auth service

type AuthHandler interface {
	Generate(context.Context, *GenerateRequest, *GenerateResponse) error
	Inspect(context.Context, *InspectRequest, *InspectResponse) error
	Refresh(context.Context, *RefreshRequest, *RefreshResponse) error
}

func RegisterAuthHandler(s server.Server, hdlr AuthHandler, opts ...server.HandlerOption) error {
	type auth interface {
		Generate(ctx context.Context, in *GenerateRequest, out *GenerateResponse) error
		Inspect(ctx context.Context, in *InspectRequest, out *InspectResponse) error
		Refresh(ctx context.Context, in *RefreshRequest, out *RefreshResponse) error
	}
	type Auth struct {
		auth
	}
	h := &authHandler{hdlr}
	return s.Handle(s.NewHandler(&Auth{h}, opts...))
}

type authHandler struct {
	AuthHandler
}

func (h *authHandler) Generate(ctx context.Context, in *GenerateRequest, out *GenerateResponse) error {
	return h.AuthHandler.Generate(ctx, in, out)
}

func (h *authHandler) Inspect(ctx context.Context, in *InspectRequest, out *InspectResponse) error {
	return h.AuthHandler.Inspect(ctx, in, out)
}

func (h *authHandler) Refresh(ctx context.Context, in *RefreshRequest, out *RefreshResponse) error {
	return h.AuthHandler.Refresh(ctx, in, out)
}
