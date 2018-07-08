from xmlrpc.server import SimpleXMLRPCServer


import datetime
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

class Node:
    def __init__(self):
        self.__atributo = None
        self.__filhos = {}
    
def retornaNo(x):
    i=0
    for x in range(0, 1000):
        for z in range(0,1000):
            i = i+x+z
    Root = Node()
    return Root


with SimpleXMLRPCServer(("192.168.0.17",8000)) as server:
    server.register_function(pow)
    server.register_function(teste, 'teste')
    server.register_function(long_8_param, 'long_8_param')
    server.register_function(long_1_param, 'long_1_param')
    server.register_function(uma_string, 'uma_string')
    server.register_function(retornaNo, 'retornaNo')

    server.register_multicall_functions()
    print('Serving XML-RPC on localhost port 7070')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        