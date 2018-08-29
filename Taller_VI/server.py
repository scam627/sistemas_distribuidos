from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

server_list = {
	"+": "8000",
	"-": "8001",
	"/": "8002",
	"*": "8003",
	"**": "8004",
	"log": "8005",
	"-/": "8006"
}

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9997), requestHandler = RequestHandler)
server.register_introspection_functions()

# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').
class MyFuncs:
	def getPort(self, op):
		return server_list[op]

server.register_instance(MyFuncs())

# Run the server's main loop
server.serve_forever()