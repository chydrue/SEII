# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:47:55 2021

@author: Cleiton Kennedy de Morais Filho
"""


import socket 
import pickle

tamanho_cabeçalho = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 3000))


while True: 
    
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg: 
            print(f"Tamanho da nova mensagem: {msg[:tamanho_cabeçalho]}")
            msglen = int(msg[:tamanho_cabeçalho])
            new_msg = False
            
        full_msg += msg
        
        if len(full_msg) - tamanho_cabeçalho == msglen:
            print("Mensagem completa recebida!")
            print(full_msg[tamanho_cabeçalho:])
            
            d = pickle.loads(full_msg[tamanho_cabeçalho:])
            print(d)
            
            new_msg = True
            full_msg = b''
    print(full_msg)
