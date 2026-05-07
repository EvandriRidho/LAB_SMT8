# remote_server.py
import socket
import pyautogui
from PIL import Image
import io
import threading
import struct

def handle_input(conn):
    """Menerima perintah mouse/keyboard dari client"""
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data: break
            # Format: "MOUSE,x,y" atau "KEY,key"
            cmd = data.split(",")
            if cmd[0] == "MOUSE":
                pyautogui.moveTo(int(cmd[1]), int(cmd[2]))
            elif cmd[0] == "CLICK":
                pyautogui.click()
        except:
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(1)
    print("[WAITING] Menunggu koneksi remote...")
    conn, addr = server.accept()
    print(f"[CONNECTED] Dikendalikan oleh {addr}")

    # Jalankan thread untuk menerima input
    threading.Thread(target=handle_input, args=(conn,), daemon=True).start()

    try:
        while True:
            # Ambil screenshot
            screen = pyautogui.screenshot()
            # Kompres ke JPEG untuk hemat bandwidth
            img_byte_arr = io.BytesIO()
            screen.save(img_byte_arr, format='JPEG', quality=50)
            data = img_byte_arr.getvalue()
            
            # Kirim ukuran data terlebih dahulu
            conn.sendall(struct.pack(">L", len(data)) + data)
    except:
        print("[DISCONNECTED] Koneksi terputus.")
        conn.close()

if __name__ == "__main__":
    main()