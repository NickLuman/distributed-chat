# -*- coding: utf-8 -*-
import socket
from threading import Thread
from tkinter import *
from tkinter import messagebox as mb


class Client:
    def __init__(self, host='', port=8765):
        self.server_addr = (host, port)

        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title("Distributed chat - Client")

        self.text = Text(width=80)

        self.frame = Frame()

        self.alias_label = Label(text="name: ")
        self.alias_input = Entry(width=10)
        self.message_label = Label(text="message: ")
        self.message_input = Entry(width=47)
        self.send_button = Button(text="send")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', 0))

        self.send_button.bind('<Button-1>', self.write)

        self.sock.sendto(('new user connected to server...').encode(
            'utf-8'), self.server_addr)

    def read(self):
        while 1:
            data = self.sock.recv(1024)
            self.text.insert(END, data.decode('utf-8') + '\n')

    def write(self, event):
        if not self.alias_input.get():
            mb.showerror("Error", "Enter username!")
            return
        if not self.message_input.get():
            mb.showerror("Error", "Enter the message!")
            return

        alias = self.alias_input.get()
        message = '{0}: {1}'.format(alias, self.message_input.get())
        self.sock.sendto((message).encode('utf-8'), self.server_addr)
        self.message_input.delete(0, 'end')

    def run_client(self):
        self.text.pack()
        self.frame.pack()

        self.alias_label.pack(side=LEFT)
        self.alias_input.pack(side=LEFT)
        self.message_label.pack(side=LEFT)
        self.message_input.pack(side=LEFT)
        self.send_button.pack(side=LEFT)

        thrd = Thread(target=self.read)
        thrd.start()

        self.root.mainloop()

        self.sock.close()
