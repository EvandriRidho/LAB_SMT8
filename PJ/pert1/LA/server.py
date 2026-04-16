import socket

HOST = '127.0.0.1'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server Kalkulator berjalan...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Terhubung: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                pesan = data.decode('utf-8')
                print(f"Data dari client: {pesan}")
                
                try:
                    allowed_chars = "0123456789+-*/. "
                    if any(c not in allowed_chars for c in pesan):
                        hasil = "Format salah!"
                    else:
                        hasil = str(eval(pesan))
                except Exception:
                    hasil = "Format salah!"
                
                conn.sendall(hasil.encode('utf-8'))

if __name__ == '__main__':
    main()