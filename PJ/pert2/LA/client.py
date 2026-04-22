import socket

HOST = '127.0.0.1'
PORT = 65432

def client():
    while True:
        try:
            domain = input("Masukkan domain: ").strip()
            if not domain:
                continue
                
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(domain.encode('utf-8'))
                
                data = s.recv(1024)
                print(f"Server: {data.decode('utf-8')}")
                
        except KeyboardInterrupt:
            print("\nKeluar dari program...")
            break
        except ConnectionRefusedError:
            print("Server tidak merespon. Pastikan kunci_server.py sudah berjalan.")
            break

if __name__ == "__main__":
    client()