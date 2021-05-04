# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:56:22 2021

@author: Cleiton Kennedy de Morais Filho
"""

import socket
import select
import errno
import sys

tamanho_cabeçalho = 10
IP = "127.0.0.1"
port = 3000

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, port))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{tamanho_cabeçalho}}".encode("utf-8")
client_socket.send(username_header + username)

while True:
    message = input(f"{my_username} > ")
    if message:
        message = message.encode("utf-8")
        message_header = f"{len(message) :< {tamanho_cabeçalho}}".encode("utf-8")
        client_socket.send(message_header + message)
    
    try:
        while True:
            #receber inputs
            username_header = client_socket.recv(tamanho_cabeçalho)
            if not len(username_header):
                print("Conexão fechada pelo servidor.")
                sys.exit()
                
            username_tamanho = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_tamanho).decode("utf-8")
            
            message_header = client_socket.recv(tamanho_cabeçalho)
            message_tamanho = int(message_header.decode("utf-8").strip())
            message = client_socket.recv(message_tamanho).decode("utf-8")
            
            print(f"{username} > {message}")
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Erro de leitura', str(e))
            sys.exit()
            
    except Exception as e:
        print('Erro geral', str(e))
        sys.exit()
        pass
        