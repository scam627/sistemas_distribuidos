from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9997), requestHandler = RequestHandler)
server.register_introspection_functions()

# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').
class MyFuncs:
	def sum(self, x, y):
		s = xmlrpclib.ServerProxy('http://localhost:8000')
		return s.calc(x, y)

server.register_instance(MyFuncs())

# Run the server's main loop
server.serve_forever()