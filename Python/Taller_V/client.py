import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:9997')

print "Envie una operacion con el siguiente formato:"
print "Numero_1 Operador Numero_2"
print "Operadores soportados:"
print "suma -> +"
print "resta -> -"
print "division -> /"
print "multiplicacion -> *"
print "potenciacion -> **"
print "radicacion -> -/"
print "logaritmacion -> log"

numbers = raw_input("> ")
print s.calc(numbers)