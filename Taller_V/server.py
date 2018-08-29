from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9997), requestHandler = RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def calc(self, numbers):
		a, op, b = numbers.split(" ")
		if op == '+':
			port = "8000"
		elif op == '-':
			port = "8001"
		elif op == '*':
			port = "8002"
		elif op == '/':
			port = "8003"
		elif op == '**':
			port = "8004"
		elif op == "-/":
			port = "8005"
		else:
			port = "8006"
		s = xmlrpclib.ServerProxy("http://localhost:" + port)
		return s.calc(a, b)

server.register_instance(MyFuncs())

# Run the server's main loop
server.serve_forever()
