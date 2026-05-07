# remote_client.py
import socket
import tkinter as tk
from PIL import Image, ImageTk
import io
import struct
import threading

def main():
    host = input("Masukkan IP Server: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 9999))

    root = tk.Tk()
    root.title("Remote Viewer")
    
    label = tk.Label(root)
    label.pack()

    def send_click(event):
        client.send(f"MOUSE,{event.x},{event.y}".encode())
        client.send("CLICK".encode())

    label.bind("<Button-1>", send_click)

    def update_screen():
        data = b""
        payload_size = struct.calcsize(">L")
        try:
            while True:
                # Ambil ukuran data
                while len(data) < payload_size:
                    data += client.recv(4096)
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack(">L", packed_msg_size)[0]

                # Ambil data gambar sesuai ukuran
                while len(data) < msg_size:
                    data += client.recv(4096)
                frame_data = data[:msg_size]
                data = data[msg_size:]

                # Tampilkan gambar
                img = Image.open(io.BytesIO(frame_data))
                img_tk = ImageTk.PhotoImage(img)
                label.config(image=img_tk)
                label.image = img_tk
        except:
            print("Koneksi terputus.")

    threading.Thread(target=update_screen, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    main()