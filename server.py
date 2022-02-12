import socket
import threading

clients = {}
addresses = {}

HOST = socket.gethostbyname(socket.gethostname())
PORT = 32000
BUFSIZ = 1024
ADDRESS = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def accept_incoming_connections():
    while True:
        client, client_address = server.accept()
        print("{}has connected".format(client_address))
        client.send(bytes("Welcome to chat now type your name and press enter", "utf8"))
        addresses[client] = client_address
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

def handle_client(client): #taking client socket as arg
    """handling each client in separate thread and if client 
       types 'quit' his connetion will be closed. 
    """
    name  = client.recv(BUFSIZ).decode("utf8")
    welcome = "Welcome {}! if wanted to quit type QUIT".format(name)
    client.send(bytes(welcome, "utf8"))
    msg = "{} had joined the chat".format(name)
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{QUIT}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{QUIT}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("{} has left the chat".format(name), "utf8"))
            break


def broadcast(msg, prefix=""):
    #prefix is just for name indentification
    #this func sends msg to all clients
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)



    