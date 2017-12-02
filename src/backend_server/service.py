import json
import operations
import pyjsonrpc
import os

config_path = os.path.join(os.path.dirname(__file__), "..", "..", "config", "config.json")
with open(config_path) as config_file:
    json_config = json.load(config_file)

config = json_config["backend_server"]

SERVER_HOST = config["HOST"]
SERVER_PORT = config["PORT"]

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    @pyjsonrpc.rpcmethod
    def submitRequestForm(self, request_form):
        return operations.submitRequestForm(request_form)
    
    @pyjsonrpc.rpcmethod
    def getRequestHistory(self, user_id):
        return operations.getRequestHistory(user_id)

    @pyjsonrpc.rpcmethod
    def deleteRequestForm(self, user_id, request_id):
        return operations.deleteRequestForm(user_id, request_id)

    @pyjsonrpc.rpcmethod
    def getRequestDetail(self, user_id, request_id):
        return operations.getRequestDetail(user_id, request_id)

HTTP_SERVER = pyjsonrpc.ThreadingHttpServer(
    server_address=(SERVER_HOST, SERVER_PORT),
    RequestHandlerClass=RequestHandler
)

print "Starting HTTP server on %s:%d" % (SERVER_HOST, SERVER_PORT)

HTTP_SERVER.serve_forever()
