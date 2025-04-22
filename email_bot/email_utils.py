import email
import email.utils
from email.header import decode_header
from email.mime.text import MIMEText
from email_bot.groq_helper import groq_call
from config import SMTP_EMAIL
import smtplib
from email.mime.multipart import MIMEMultipart
from email_bot.config import SMTP_EMAIL, SMTP_PASSWORD


def parse_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True).decode()
    else:
        return msg.get_payload(decode=True).decode()
    return ""


def get_sender(msg):
    from_header = msg.get("From")
    return email.utils.parseaddr(from_header)[1]


def generate_reply(content):
    return groq_call(content)


def send_email(subject, body, recipient):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = SMTP_EMAIL
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))  # Attach body as plain text

    # Setup the server and send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # Gmail SMTP server and SSL port
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(SMTP_EMAIL, recipient, msg.as_string())
            print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Error sending email: {e}")