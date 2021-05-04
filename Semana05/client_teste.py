# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:12:56 2021

@author: Cleiton Kennedy de Morais Filho
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 3000))

msg = s.recv(1024)
print(msg.decode("utf-8"))

      