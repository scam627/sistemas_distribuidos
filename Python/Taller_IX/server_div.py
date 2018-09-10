import socket
import math
import thread

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("localhost", 8002))
my_socket.listen(1)

def service(client_socket, addr):
    numeros = client_socket.recv(1024)
    a, op, b = numeros.split(" ")
    print str(addr[0]) + " dice: ", a, " ", b
    resultado = float(a) / float(b)
    client_socket.send(str(resultado))
    client_socket.close()

while True:
    client_socket, addr = my_socket.accept()
    thread.start_new_thread(service, (client_socket, addr))
    
