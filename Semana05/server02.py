# -*- coding: utf-8 -*-
"""
Created on Mon May  3 18:45:40 2021

@author: Cleiton Kennedy de Morais Filho
"""

import socket 

tamanho_cabeçalho = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3000))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Conexão com {address} estabelecida!!!")
    
    msg = "Bem vindo ao servidor!"
    msg = f'{len(msg):<{tamanho_cabeçalho}}' + msg
    
    clientsocket.send(bytes(msg, "utf-8"))
    
    