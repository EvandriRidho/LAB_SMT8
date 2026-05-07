import smtplib
import mimetypes
import re
import os
from datetime import datetime
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'evandriridho555@gmail.com'
SMTP_PASSWORD = 'obrq bnid iety utqx'  

email_to = [
    'andhikagaluh15@gmail.com', 'faididid@gmail.com', 'af196869@gmail.com',
    'sandholley@gmail.com', 'recipient5@icloud.com', 'recipient6@protonmail.com',
    'recipient7@example.com'
]
email_cc = [
    'cc1@gmail.com', 'cc2@yahoo.com', 'cc3@outlook.com', 
    'cc4@hotmail.com', 'cc5@icloud.com'
]
email_bcc = [
    'bcc1@gmail.com', 'bcc2@yahoo.com'
]


def is_valid_email(email):
    """Validate email format for any domain."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_subject(subject):
    """Validate subject: not empty and reasonable length."""
    if not subject or len(subject.strip()) == 0:
        return False, "Subject cannot be empty."
    if len(subject) > 255:
        return False, "Subject is too long."
    return True, "Valid"


def compose_email(subject, body, attachments=None):
    # Validate Subject
    is_valid, msg_error = is_valid_subject(subject)
    if not is_valid:
        print(f"Validation Error: {msg_error}")
        return None

    # Filter Valid Emails
    valid_to = [e for e in email_to if is_valid_email(e)]
    valid_cc = [e for e in email_cc if is_valid_email(e)]
    valid_bcc = [e for e in email_bcc if is_valid_email(e)]

    if not valid_to:
        print("Error: No valid 'To' recipients found.")
        return None

    # Create Message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SMTP_USERNAME
    msg['To'] = ', '.join(valid_to)
    msg['Cc'] = ', '.join(valid_cc)
    msg['Bcc'] = ', '.join(valid_bcc)
    msg.set_content(body)

    # Handle Attachments
    if attachments:
        for file_path in attachments:
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'rb') as f:
                        file_data = f.read()
                        file_name = os.path.basename(file_path)
                        mime_type, _ = mimetypes.guess_type(file_path)
                        if mime_type is None:
                            mime_type = 'application/octet-stream'
                        
                        maintype, subtype = mime_type.split('/', 1)
                        msg.add_attachment(
                            file_data, 
                            maintype=maintype, 
                            subtype=subtype, 
                            filename=file_name
                        )
                        print(f"Attachment added: {file_name}")
                except Exception as e:
                    print(f"Could not attach file {file_path}: {e}")
            else:
                print(f"Warning: Attachment file not found: {file_path}")

    return msg

def send_email(msg):
    if msg is None:
        return

    try:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Connecting to server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Email sent successfully!")
        print(f"Total recipients: To({len(email_to)}), CC({len(email_cc)}), BCC({len(email_bcc)})")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    subject_text = "LA4"
    body_text = """Halo semua,
    Ini adalah email otomatis yang dikirim menggunakan Python.
    Terima kasih."""

    # Path to attachment (ensure the file exists)
    attachment_files = ['gambar.JPG'] 

    # Execute
    message = compose_email(subject_text, body_text, attachment_files)
    send_email(message)