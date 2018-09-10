import socket

server_list = [8000,8001,8002,8003,8004,8005,8006]

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("localhost", 9999))
my_socket.listen(1)
client_socket, addr = my_socket.accept()
while True:
    numeros = client_socket.recv(1024)
    if numeros == "close":
        break
    a, op, b = numeros.split(" ")
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if op == "+":
        socket_server.connect(("localhost",server_list[0]))
    elif op == "-":
        socket_server.connect(("localhost",server_list[1]))
    elif op == "/":
        socket_server.connect(("localhost",server_list[2]))
    elif op == "*":
        socket_server.connect(("localhost",server_list[3]))
    elif op == "**":
        socket_server.connect(("localhost",server_list[4]))
    elif op == "log":
        socket_server.connect(("localhost",server_list[5]))
    elif op == "-/":
        socket_server.connect(("localhost",server_list[6]))
    socket_server.send(numeros)
    resultado = socket_server.recv(1024)
    socket_server.close()
    client_socket.send(str(resultado))
print "Adios."
client_socket.close()
my_socket.close()
