import imaplib
import smtplib
from email.message import EmailMessage
from email.parser import BytesParser
from email.header import decode_header

from email_bot.config import SMTP_EMAIL, SMTP_PASSWORD  # import your credentials


def get_email_content(sender_email):
    imap_server = "imap.gmail.com"
    imap = imaplib.IMAP4_SSL(imap_server)

    # Login using app password
    imap.login(SMTP_EMAIL, SMTP_PASSWORD)

    # Select inbox
    imap.select("inbox")

    # Search for emails from specific sender
    status, messages = imap.search(None, f'FROM "{sender_email}"')
    email_ids = messages[0].split()

    if not email_ids:
        print("No emails found from:", sender_email)
        return None

    # Get the latest email
    latest_email_id = email_ids[-1]
    status, msg_data = imap.fetch(latest_email_id, "(RFC822)")
    raw_email = msg_data[0][1]

    # Parse email
    parser = BytesParser()
    msg = parser.parsebytes(raw_email)

    # Get plain text body
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                return part.get_payload(decode=True).decode()
    else:
        return msg.get_payload(decode=True).decode()

    imap.logout()


def send_email(to, subject, body):
    msg = EmailMessage()
    msg["From"] = SMTP_EMAIL
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(SMTP_EMAIL, SMTP_PASSWORD)
        smtp.send_message(msg)
