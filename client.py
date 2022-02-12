import socket
import tkinter


BUFSIZ = 1024

def receive():
    """Handles receiving of msg"""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            #if client has left the chat it may raise error
            break

def send(): 
    pass