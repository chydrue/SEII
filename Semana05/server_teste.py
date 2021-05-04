# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:47:31 2021

@author: Cleiton Kennedy de Morais Filho
"""

import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3000))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Conexão com {address} foi estabelecida!")
    clientsocket.send(bytes("Bem vindo ao servidor!", "utf-8"))
    