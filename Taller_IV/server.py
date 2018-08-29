from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000), requestHandler = RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def calc(self, numbers):
		a, op, b = numbers.split(" ")
		if op == '+':
			return int(a) + int(b)
		elif op == '-':
			return int(a) - int(b)
		elif op == '*':
			return int(a) * int(b)
		elif op == '/':
			return float(a) / float(b)
		elif (op == '**'):
			return int(a) ** int(b)
		else:
			return float(b) ** (1 / float(a))

server.register_instance(MyFuncs())

# Run the server's main loop
server.serve_forever()
