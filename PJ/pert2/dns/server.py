import socket

DNS_TABLE = {
    "www.google.com": "192.168.1.1",
    "www.facebook.com": "192.168.1.2",
    "www.yahoo.com": "192.168.1.3",
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 53))

print("DNS Server is running...")

while True:
    data, address = server_socket.recvfrom(1024)
    domain_name = data.decode("utf-8")

    if domain_name in DNS_TABLE:
        ip_address = DNS_TABLE[domain_name]
    else:
        ip_address = "Domain not found"

    server_socket.sendto(ip_address.encode("utf-8"), address)