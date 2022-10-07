from socket import *
import sys
import time

# create client socket
client_socket = socket(AF_INET, SOCK_DGRAM)
#print("Socket has been created\n")

n = len(sys.argv)
if(n!=4):
    print("Number of arguments is too short or too long.\nSpecify IP, Port, and Object")
    exit()

server_ip = sys.argv[1]
server_port = sys. argv[2]
#number of pings
number = sys.argv[3]

Lost = 0
receive = 0
time_list = []

print(f"Pinging {server_ip}:")

for i in range(int(number)):
    time.sleep(1)
    start_time = time.time()
    client_socket.sendto(("Ping").encode(), (server_ip, int(server_port)))
    recv_message, server_address = client_socket.recvfrom(2048)
    msg = recv_message.decode()
    if(msg == "Request timed out"):
        Lost += 1
        print("Request timed out.")
    else:
        end_time = time.time()
        total = (end_time - start_time )* 1000
        time_list.append(total)
        receive += 1
        print(f"Reply from {server_address[0]}: Ping {i+1} {msg} time={total:.3f}ms TTL=64")

print(f"\nPing statistics from {server_address}")
print(f"\tSegments: Sent: {number}, Received: {receive}, Lost: {Lost} ({int(Lost)/int(number) * 100}% Loss)")
print("Approximate round trip times in ms:")
print(f"Minimum = {min(time_list):.3f}ms, Maximum = {max(time_list):.3f}ms, Average = {sum(time_list)/len(time_list):.3f}ms")


# close client socket
client_socket.close()
