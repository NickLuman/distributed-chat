# -*- coding: utf-8 -*-
import argparse
from server import Server
from client import Client


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
        server = Server(args.host, args.port)
