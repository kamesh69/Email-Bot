import imaplib
import smtplib
from email_bot import config

def connect_imap():
    mail = imaplib.IMAP4_SSL(config.IMAP_SERVER)
    mail.login(config.SMTP_EMAIL, config.SMTP_PASSWORD)
    return mail

def connect_smtp():
    smtp = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
    smtp.starttls()
    smtp.login(config.SMTP_EMAIL, config.SMTP_PASSWORD)
    return smtp