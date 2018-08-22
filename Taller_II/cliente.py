import socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.connect(("localhost", 9997))
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
while True:
    numeros = raw_input("> ")
    socket_server.send(numeros)
    print "=> ", socket_server.recv(1024)
    if numeros == "close":
        break
print "Adios."
socket_server.close()
