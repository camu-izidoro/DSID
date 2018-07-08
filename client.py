import xmlrpc.client
import time
from datetime import datetime
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

##função inutil na execução
inid = time.time() 
sd= xmlrpc.client.ServerProxy('http://192.168.0.17:8000')
try:
    sd.teste()
except xmlrpc.client.Fault as err:
    h=1
fimd = time.time()
print("DESCARTAR Função teste PARAMETRO E RETURN : ", fimd-inid)

ini = time.time() 
s4= xmlrpc.client.ServerProxy('http://192.168.0.17:8000')
try:
  z =  s4.long_1_param(123223423)
except xmlrpc.client.Fault as err:
    print("A fault occurred")
    print("Fault code: %d" % err.faultCode)
    print("Fault string: %s" % err.faultString)
fim = time.time()
print("Função C 1 PARAMETRO E RETURN : ", fim-ini)

ini3 = time.time() 
s1 = xmlrpc.client.ServerProxy('http://192.168.0.17:8000')
try:
   s1.c_void()
except xmlrpc.client.Fault as err:
    h=1
fim3 = time.time()
print("Função c void", fim3- ini3)

ini2 = time.time() 
s = xmlrpc.client.ServerProxy('http://192.168.0.17:8000')
try:
   x= s.long_8_param(123223423,123223423,123223423,123223423,123223423,123223423,123223423,123223423)
except xmlrpc.client.Fault as err:
    print("A fault occurred")
    print("Fault code: %d" % err.faultCode)
    print("Fault string: %s" % err.faultString)
fim2 = time.time()
print("Função C 8 PARAMETROS E 1 RETURN ", fim2- ini2)


class Node:
    def __init__(self):
        self.__atributo = 1

No = Node()
No.__atributo=1
ini4 = time.time() 

s2= xmlrpc.client.ServerProxy('http://192.168.0.17:8000')
try:
  x= s2.retornaNo(No)
except xmlrpc.client.Fault as err:
    h=1
fim4 = time.time()
print("Função c tipo complexo", fim4- ini4)


ini5 = time.time() 
s5 = xmlrpc.client.ServerProxy('http://192.168.0.17:8000')
try:
  x= s5.uma_string('aadorq3942894jtuehfsurhwuer')
except xmlrpc.client.Fault as err:
    print("excecao")
    h=1
fim5 = time.time()
print("Função c 1 string retorna 1 string", fim5 - ini5)

ini6 = time.time() 
s6 = xmlrpc.client.ServerProxy('http://192.168.0.17:8000')
try:
  x= s6.oito_string('aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer')
except xmlrpc.client.Fault as err:
    print("excecao")
    h=1
fim6 = time.time()
print("Função c 8 string retorna 1 string", fim6 - ini6)

ini7 = time.time() 
s7 = xmlrpc.client.ServerProxy('http://192.168.0.17:8000')
try:
  x= s7.dezeseis_string('aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer')
except xmlrpc.client.Fault as err:
    print("excecao")
    h=1
fim7 = time.time()
print("Função c 16 string retorna 1 string", fim7 - ini7)

ini8 = time.time() 
s8 = xmlrpc.client.ServerProxy('http://192.168.0.17:8000')
try:
  x= s8.trintaeduas_string('aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer','aadorq3942894jtuehfsurhwuer')
except xmlrpc.client.Fault as err:
    print("excecao")
    h=1
fim8 = time.time()
print("Função c 32 string retorna 1 string", fim8 - ini8)

arrayTeste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
ini9 = time.time() 
s9 = xmlrpc.client.ServerProxy('http://192.168.0.17:8000')
try:
  x= s9.vetor(arrayTeste)
except xmlrpc.client.Fault as err:
    print("excecao")
    h=1
fim9 = time.time()
print("Função c vetor retorna vetor", fim9 - ini9)

num = input("Digite x para fechar:")
print(num)