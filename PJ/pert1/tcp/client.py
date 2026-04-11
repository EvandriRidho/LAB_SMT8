import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9000))

message = client_socket.recv(1024)
print(message.decode('utf-8'))