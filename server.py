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
    name  = client.recv(BUFSIZ).decode("utf8")
    welcome = "Welcome {}! if wanted to quit type QUIT".format(name)
    client.send(bytes(welcome, "utf8"))
    msg = "{} had joined the chat".format(name)
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    