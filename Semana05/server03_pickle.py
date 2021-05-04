# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:43:29 2021

@author: Cleiton Kennedy de Morais Filho
"""

import socket
import pickle


tamanho_cabeçalho = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3000))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Conexão com {address} estabelecida!!!")
    
    d = {1: "Olá", 2: "Como vai?"}
    msg = pickle.dumps(d)

    
    msg = bytes(f'{len(msg):<{tamanho_cabeçalho}}', "utf-8") + msg
    
    clientsocket.send(msg)