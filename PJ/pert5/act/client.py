import socket
import os

PORT = 5050
# Ganti SERVER dengan alamat IP server jika dijalankan di komputer berbeda
SERVER = "172.20.10.2" #ipconfig di terminal yg ipv4 
ADDR = (SERVER, PORT)
SEPARATOR = "<SEPARATOR>"
CHUNKSIZE = 4 * 1024

def send_file(conn, filename):
    filesize = os.path.getsize(filename)
    # Kirim nama file dan ukurannya ke server
    conn.send(f"{filename}{SEPARATOR}{filesize}".encode())

    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(CHUNKSIZE)
            if not bytes_read:
                break
            conn.sendall(bytes_read)

def receive_file(conn):
    # Terima nama file dan ukurannya
    data = conn.recv(1024).decode()
    filename, filesize = data.split(SEPARATOR)
    
    filename = os.path.basename(filename)
    filesize = int(filesize)

    with open(filename, "wb") as f:
        while True:
            bytes_read = conn.recv(CHUNKSIZE)
            if not bytes_read:
                break
            f.write(bytes_read)

def send_file_to_server(filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    client.send("RECEIVE".encode())  # ← server akan RECEIVE
    response = client.recv(1024).decode()

    if response == "OK":
        send_file(client, filename)  # client kirim file
        print(f"[SUCCESS] '{filename}' terkirim ke server.")

    client.close()

def receive_file_from_server(filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    client.send("SEND".encode())  # ← server akan SEND
    response = client.recv(1024).decode()

    if response == "OK":
        client.send(filename.encode())
        receive_file(client)  # client terima file
        print(f"[SUCCESS] File diterima dari server.")

    client.close()

if __name__ == "__main__":
    # Pastikan file.txt ada di folder yang sama sebelum menjalankan send_file_to_server
    send_file_to_server("file.txt") 
    
    # Atau jika ingin mengambil file dari server
    receive_file_from_server("file.txt")
    
    pass # Ganti dengan fungsi yang ingin kamu jalankan