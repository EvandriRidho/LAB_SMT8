import socket

def main():
    host = input("Masukkan IP host: ")
    if not host: host = "127.0.0.1"
    port = 5050
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        
        while True:
            guess = input("Masukkan tebakan (1-100): ")
            if not guess: continue
            
            client.send(guess.encode('utf-8'))
            response = client.recv(1024).decode('utf-8')
            print(response)
            
            if "BENAR!" in response:
                print(f"[SERVER]: Player {client.getsockname()} menang!")
                break
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()