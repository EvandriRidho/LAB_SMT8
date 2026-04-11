import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "Halo udp server"
client_socket.sendto(message.encode('utf-8'), ('localhost', 9001))
data, address = client_socket.recvfrom(1024)
print(data.decode('utf-8'))