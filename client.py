import xmlrpc.client
import time
from datetime import datetime
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

s = xmlrpc.client.ServerProxy('http://192.168.0.17:8000')
ini = time.time() 
try:
  z =  s.long_1_param(123223423)
except xmlrpc.client.Fault as err:
    print("A fault occurred")
    print("Fault code: %d" % err.faultCode)
    print("Fault string: %s" % err.faultString)
fim = time.time()
print("Função C 1 PARAMETRO E RETURN : ", fim-ini)

ini2 = time.time() 
try:
   x= s.long_8_param(123223423,123223423,123223423,123223423,123223423,123223423,123223423,123223423)
except xmlrpc.client.Fault as err:
    print("A fault occurred")
    print("Fault code: %d" % err.faultCode)
    print("Fault string: %s" % err.faultString)
fim2 = time.time()
print("Função C 8 PARAMETROS E 1 RETURN ", fim2- ini2)

ini3 = time.time() 
try:
   s.teste()
except xmlrpc.client.Fault as err:
    h=1
fim3 = time.time()
print("Função c void", fim3- ini3)

ini4 = time.time() 
try:
  x= s.retornaNo('abcd')
except xmlrpc.client.Fault as err:
    h=1
fim4 = time.time()
print("Função c tipo complexo", fim4- ini4)


ini5 = time.time() 
try:
  x= s.uma_string('aadorq3942894jtuehfsurhwuer')
except xmlrpc.client.Fault as err:
    h=1
fim5 = time.time()
print("Função c string", fim5 - ini5)

num = input("Digite x para fechar:")
print(num)