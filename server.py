# -*- coding: utf-8 -*-
import socket
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

        while 1:
            data = None
            try:
                data, address = self.sock.recvfrom(1024)
            except socket.error:
                pass
            finally:
                timer_buffer = self.timer_point.recv()

                if data:
                    print("address: {0}, {1}; message: {2} ---- {3}".format(address[0], address[1], str(timer_buffer), data.decode('utf-8')))

                    message_for_all = ("{0} {1}".format(
                        str(timer_buffer), data.decode('utf-8'))).encode('utf-8')

                    if address not in self.clients:
                        self.clients.append(address)
                    for client in self.clients:
                        self.sock.sendto(message_for_all, client)
