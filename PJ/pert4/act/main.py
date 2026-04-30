import smtplib
import mimetypes
from email.message import EmailMessage

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'evandriridho555@gmail.com'
smtp_password = 'obrq bnid iety utqx'
email = ['faididid@gmail.com', 'evandriridho321@gmail.com', 'andhikagaluh15@gmail.com', 'faidwijaya@gmail.com', 'af196869@gmail.com']

gmail_only = [e for e in email if e.lower().endswith('@gmail.com')]

msg = EmailMessage()
msg['From'] = smtp_username
msg['To'] = ','.join(gmail_only) # Mengirim hanya ke gmail saja
msg['Subject'] = 'Hello, World!'
msg['cc'] = 'faidwijaya@gmail.com'
msg.set_content('This is a test email.')

# --- TAMBAHAN UNTUK ATTACHMENT ---
files = ['gambar.JPG'] # Ganti dengan nama file fotomu jika berbeda

for file in files:
    try:
        with open(file, 'rb') as f:
            file_data = f.read()
            mime_type, _ = mimetypes.guess_type(file)
            if mime_type:
                maintype, subtype = mime_type.split('/', 1)
            else:
                maintype, subtype = 'application', 'octet-stream'
            
            msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file)
            print(f"Berhasil melampirkan: {file}")
    except FileNotFoundError:
        print(f"Peringatan: File {file} tidak ditemukan.")

print("Sedang mengirim email...")
try:
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.send_message(msg)
    print("Email berhasil dikirim ke semua penerima!")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")