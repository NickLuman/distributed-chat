# -*- coding: utf-8 -*-
import argparse
from server import Server
from client import Client
from timer import Timer
from multiprocessing import Process, Pipe

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--type", default="server", type=str, help="Input type of usage client/server.")
    parser.add_argument("--host", default='', type=str, help="Input host connection.")
    parser.add_argument("--port", default=8765, type=int, help="Input port for connection.")
    
    args = parser.parse_args()

    if args.type == "client":
        client = Client(args.host, args.port)
        client.run_client()
    elif args.type == "server":
        timer_point, server_point = Pipe()

        server = Server(timer_point, args.host, args.port)
        server.start()

        timer = Timer(server_point)
        timer.start()

        server.join()
        timer.join()
