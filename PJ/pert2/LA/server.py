import socket


HOST = '127.0.0.1'
PORT = 65432


BLOCKED_DOMAINS = ['weibo.com', 'bilibili.tv', 'aipac.org']

def start_server():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("DNS Server berjalan...")
        
        while True:
            
            conn, addr = s.accept()
            with conn:
                print(f"Terhubung: {addr}")
                data = conn.recv(1024)
                
                if data:
                    domain = data.decode('utf-8').strip()
                    print(f"Request domain: {domain}")
                    
                    
                    if domain in BLOCKED_DOMAINS:
                        response = "Domain diblokir!"
                    else:
                        try:
                            
                            ip = socket.gethostbyname(domain)
                            response = f"IP {domain} = {ip}"
                        except socket.gaierror:
                            
                            response = "Domain tidak ditemukan!"
                    
                    
                    conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()