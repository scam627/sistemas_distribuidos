import socket
import math

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("localhost", 9997))
my_socket.listen(1)
client_socket, addr = my_socket.accept()

while True:
    numeros = client_socket.recv(1024)
    if numeros == "close":
        break
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
print "Adios."
client_socket.close()
my_socket.close()
