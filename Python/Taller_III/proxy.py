import socket

server_list = {
	"+": 8000,
	"-": 8001,
	"/": 8002,
	"*": 8003,
	"**": 8004,
	"log": 8005,
	"-/": 8006
}

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("localhost", 9990))
my_socket.listen(1)
client_socket, addr = my_socket.accept()
op = client_socket.recv(1024)
client_socket.send(str(server_list[op]))
print "Adios."
client_socket.close()
my_socket.close()