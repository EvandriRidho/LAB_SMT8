import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 9001))

print("Listening port 9000")
while True:
    data, address = server_socket.recvfrom(1024)
    print('Recaived message', data.decode('utf-8'), 'from' , address)
    server_socket.sendto(data, address)