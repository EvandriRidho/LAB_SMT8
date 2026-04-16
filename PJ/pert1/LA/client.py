import socket

HOST = '127.0.0.1'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        while True:
            try:
                operasi = input("Masukkan operasi (contoh: 10 + 5): ")
                
                if not operasi.strip():
                    continue
                    
                s.sendall(operasi.encode('utf-8'))
                
                data = s.recv(1024)
                print(f"Hasil: {data.decode('utf-8')}")
                
            except KeyboardInterrupt:
                print("\nKeluar dari kalkulator.")
                break

if __name__ == '__main__':
    main()