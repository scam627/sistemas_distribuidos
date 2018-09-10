import socket
import thread 
import math

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("localhost", 9998))
my_socket.listen(1)

def service(client_socket, addr):
    numeros = client_socket.recv(1024)
    a,op,b = numeros.split(" ")
    print str(addr[0]) + " dice: ", a ," ",b 
    if op == "+":
        resultado = int(a) + int(b)
    elif op == "-":
        resultado = int(a) - int(b)
    elif op == "/":
        resultado = float(a) / float(b)
    elif op == "*":
        resultado = int(a) * int(b)
    elif op == "**":
        resultado = int(a) ** int(b)
    elif op == "log":
        resultado = math.log(float(b), float(a))
    elif op == "-/":
        resultado = float(b) ** ( 1/float(a))
    client_socket.send(str(resultado))

while True:
    client_socket, addr = my_socket.accept()
    print "Client Connected: IP -> " + str(addr[0]) + " Puerto -> " + str(addr[1])
    thread.start_new_thread(service,(client_socket, addr))


print "Adios"
client_socket.close()
my_socket.close() 