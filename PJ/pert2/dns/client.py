import socket

SERVER_IP_ADDRESS = "localhost"

DOMAIN_NAME = 'www.google.com'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto(DOMAIN_NAME.encode("utf-8"), (SERVER_IP_ADDRESS, 53))

response, _ = client_socket.recvfrom(1024)

ip_address = response.decode("utf-8")
print(f"The IP address for {DOMAIN_NAME} is: {ip_address}")