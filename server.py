# -*- coding: utf-8 -*-
import socket

class Server(object):
    def __init__(self, host='', port=8765):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((host, port))
        client = []  
        print('Start Server')
        while 1:
            data, addres = sock.recvfrom(1024)
            print(addres[0], addres[1])
            if addres not in client:
                client.append(addres)
            for clients in client:
                if clients == addres:
                    continue  
                sock.sendto(data, clients)

    
