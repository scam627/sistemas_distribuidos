import socket

socket_proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_proxy.connect(("localhost", 9990))

print "Envie una operacion con el siguiente formato:"
print "Numero_1 Operador Numero_2"
print "Operadores permitidos:"
print "suma -> +"
print "resta -> -"
print "division -> /"
print "multiplicacion -> *"
print "potenciacion -> **"
print "radicacion -> -/"
print "logaritmacion -> log"

numeros = raw_input("> ")
a, op, b = numeros.split(" ")
socket_proxy.send(op)
port_op = socket_proxy.recv(1024)
socket_op = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_op.connect(("localhost", int(port_op)))
socket_op.send(numeros)
print "=> ", socket_op.recv(1024)
print "Adios."
socket_proxy.close()
