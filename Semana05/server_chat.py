# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:55:58 2021

@author: Cleiton Kennedy de Morais Filho
"""

import socket
import select

tamanho_cabeçalho = 10
IP = "127.0.0.1"
port = 3000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, port))

server_socket.listen()

sockets_list = [server_socket]

clients = {}



def receive_message(client_socket):
    try:
        cabeçalho_mensagem = client_socket.recv(tamanho_cabeçalho)
        
        if not len(cabeçalho_mensagem):
            return False
        
        tamanho_mensagem = int(cabeçalho_mensagem.decode('utf-8').strip())
        return {'cabeçalho': cabeçalho_mensagem, 'conteúdo': client_socket.recv(tamanho_mensagem)}
    
    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            
            user = receive_message(client_socket)
            if user is False: 
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            
            print(f"Nova conexão aceita de {client_address[0]}:{client_address[1]} username: {user['conteúdo'].decode('utf-8')}")
        else:
            message = receive_message(notified_socket)
            if message is False:
                print(f"Conexão fechada com {clients[notified_socket]['conteúdo'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            
            user = clients[notified_socket]
            
            print(f"Mensagem recebida de {user['conteúdo'].decode('utf-8')}: {message['conteúdo'].decode('utf-8')}")
            
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['cabeçalho'] + user['conteúdo'] + message['cabeçalho'] + message['conteúdo'])
    
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
        