import socket
import threading
import os

PORT = 5050
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)
SEPARATOR = "<SEPARATOR>"
CHUNKSIZE = 4 * 1024  # 4KB

def send_file(conn, filename):
    filesize = os.path.getsize(filename)
    # Mengirim metadata (nama file dan ukuran)
    conn.send(f"{filename}{SEPARATOR}{filesize}".encode())

    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(CHUNKSIZE)
            if not bytes_read:
                # File selesai dibaca
                break
            conn.sendall(bytes_read)

def receive_file(conn):
    data = conn.recv(1024).decode()
    filename, filesize = data.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    received = 0
    with open(filename, "wb") as f:
        while received < filesize:
            chunk = min(CHUNKSIZE, filesize - received)
            bytes_read = conn.recv(chunk)
            if not bytes_read:
                break
            f.write(bytes_read)
            received += len(bytes_read)
    print(f"[DONE] '{filename}' tersimpan ({received} bytes)")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            if data == "SEND":
                conn.send("OK".encode())
                # Server akan mengirim file ke client
                filename = conn.recv(1024).decode()
                send_file(conn, filename)
                
            elif data == "RECEIVE":
                conn.send("OK".encode())
                # Server akan menerima file dari client
                receive_file(conn)
            
            else:
                # Jika command tidak dikenal atau client kirim sinyal putus
                break
        except Exception as e:
            print(f"[ERROR] {e}")
            break

    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()