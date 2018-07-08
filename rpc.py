from xmlrpc.server import SimpleXMLRPCServer
from array import array

import datetime
def c_void():
    i=0
    for x in range(0, 1000):
        for z in range(0,1000):
            i = i+x+z

def teste():
    i=0
    for x in range(0, 1000):
        for z in range(0,1000):
            i = i+x+z            

def long_8_param(a,b,c,d,e,f,g,h):
    i=0
    for x in range(0, 1000):
        for z in range(0,1000):
            i = i+x+z
    return a

def long_1_param(a):
    i=0
    for x in range(0, 1000):
        for z in range(0,1000):
            i = i+x+z
    return a

def uma_string(a):
    i=0
    for x in range(0, 1000):
        for z in range(0,1000):
            i = i+x+z
    return a

def oito_string(a,b,c,d,e,f,g,h):
    i=0
    for x in range(0, 1000):
        for z in range(0,1000):
            i = i+x+z
    return a

def dezeseis_string(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    i=0
    for x in range(0, 1000):
        for z in range(0,1000):
            i = i+x+z
    return a

def trintaeduas_string(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,y,z,w,aa,ab,ac,ad,ae,af):
    i=0
    for x in range(0, 1000):
        for z in range(0,1000):
            i = i+x+z
    return a

class Node:
    def __init__(self):
        self.__atributo = 1
    
def retornaNo(obj):
    i=0
    for x in range(0, 1000):
        for z in range(0,1000):
            i = i+x+z
    return obj

def vetor(a):
    i=0
    for x in range(0, 1000):
        for z in range(0,1000):
            i = i+x+z
    return a


with SimpleXMLRPCServer(("192.168.0.17",8000)) as server:
    server.register_function(pow)
    server.register_function(teste, 'teste')
    server.register_function(c_void, 'c_void')
    server.register_function(long_8_param, 'long_8_param')
    server.register_function(long_1_param, 'long_1_param')
    server.register_function(uma_string, 'uma_string')
    server.register_function(oito_string, 'oito_string')
    server.register_function(dezeseis_string, 'dezeseis_string')
    server.register_function(trintaeduas_string, 'trintaeduas_string')
    server.register_function(retornaNo, 'retornaNo')
    server.register_function(vetor,'vetor')

    server.register_multicall_functions()
    print('Serving XML-RPC on localhost port 8000')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        