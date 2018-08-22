import socket
import math

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("localhost", 8000))
my_socket.listen(1)

while True:
    client_socket, addr = my_socket.accept()
    numeros = client_socket.recv(1024)
    a, op, b = numeros.split(" ")
    print str(addr[0]) + " dice: ", a, " ", b
    resultado = int(a) + int(b)
    client_socket.send(str(resultado))
    client_socket.close
