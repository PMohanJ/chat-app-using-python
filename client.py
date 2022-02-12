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

def send(event=None):
    #event is passed by binders.
    msg = my_msg.get()
    my_msg.set("") #clearing the input field
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{QUIT}":
        client_socket.close()
        top.quit()

 
    