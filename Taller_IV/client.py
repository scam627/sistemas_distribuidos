import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:9997')
print s.sum(5, 2)