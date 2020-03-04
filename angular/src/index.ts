import { Injectable } from "@angular/core";
import { HttpClient, HttpParams, HttpHeaders } from "@angular/common/http";

const defaultLocal = "http://localhost:8080/client";
const defaultLive = "https://api.micro.mu/client";

export interface Options {
  token?: string;
  // Address of the micro platform.
  // By default it connects to live. Change it or use the local flag
  // to connect to your local installation.
  address?: string;
  // Helper flag to help users connect to the default local address
  local?: boolean;
}

export interface ClientRequest {
  // eg. "go.micro.srv.greeter"
  service: string;
  // eg. "Say.Hello"
  endpoint: string;
  // json and then base64 encoded body
  body: string;
}

export interface ClientResponse {
  // json and base64 encoded response body
  body: string;
}

@Injectable()
export class Client {
  public options: Options = {
    address: defaultLive
  };

  constructor(private http: HttpClient) {}

  setOptions(options: Options) {
    if (options) {
      this.options = options;
    }
    if (options && options.local) {
      this.options.address = defaultLocal;
    }
  }

  // Call enables you to access any endpoint of any service on Micro
  call<R>(service: string, endpoint: string, request?: any): Promise<R> {
    return new Promise<R>(async (resolve, reject) => {
      try {
        // example curl: curl -XPOST -d '{"service": "go.micro.srv.greeter", "endpoint": "Say.Hello"}'
        //  -H 'Content-Type: application/json' http://localhost:8080/client {"body":"eyJtc2ciOiJIZWxsbyAifQ=="}
        if (!request) {
          request = {};
        }
        const serviceReq: ClientRequest = {
          service: service,
          endpoint: endpoint,
          body: Buffer.from(JSON.stringify(request)).toString("base64")
        };
        var options = {
          headers: {
            micro_token: this.options.token as string
          }
        };

        const result = await this.http
          .post<ClientResponse>(
            this.options.address as string,
            serviceReq,
            options
          )
          .toPromise();
        resolve(JSON.parse(Buffer.from(result.body, "base64").toString()));
      } catch (e) {
        reject(e);
      }
    });
  }
}
