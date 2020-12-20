# -*- coding: utf-8 -*-
import socket
import select
from multiprocessing import Process

class Server(Process):
    def __init__(self, timer_point, host='', port=8765):
        Process.__init__(self)
        self.timer_point = timer_point
        self.host = host
        self.port = port

        self.clients = []

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        self.sock.setblocking(0)
        self.daemon = True       

    def run(self):
        print("Server is running...")

        poller = select.poll()
        poller.register(self.sock, select.POLLIN)
        poller.register(self.timer_point, select.POLLIN)
        self.sock.fileno()
        
        timer_buffer = None

        while 1:
            data = None

            socket_Event = poller.poll(1000)
            for descriptor, Event in socket_Event:
                if descriptor == self.timer_point.fileno():
                    timer_buffer = self.timer_point.recv()
                if descriptor == self.sock.fileno():
                    data, address = self.sock.recvfrom(1024)
                    self.send_to_all(timer_buffer, data, address)

    def send_to_all(self, timer_buffer, data, address):
        message_for_all = ("{0} {1}".format(
            str(timer_buffer), data.decode('utf-8'))).encode('utf-8')

        print("address: {0}, {1}; message: {2} ---- {3}".format(
            address[0], address[1], str(timer_buffer), data.decode('utf-8')))
        
        if address not in self.clients:
            self.clients.append(address)
        for client in self.clients:
            self.sock.sendto(message_for_all, client)



