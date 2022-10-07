from socket import *
from random import randint
from datetime import datetime

# create server socket
server_socket = socket(AF_INET, SOCK_DGRAM)
# bind server socket to port number
server_socket.bind(('', 12000))
print("Server is ready to receive messages...\n")

# run forever loop to keep receiving messages
while (True):

    message, client_address = server_socket.recvfrom(2048)
    num = randint(1,11)

    if(num<=4):
        server_socket.sendto("Request timed out".encode(), client_address)
    else:
        today = datetime.now().strftime("%a %b %d %I:%M:%S %Y")
        server_socket.sendto(today.encode(), client_address)

