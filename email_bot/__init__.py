# email_bot/__init__.py

from email_bot.gmail_helper import get_email_content, send_email
from email_bot.openai_helper import generate_reply
from email_bot.groq_helper import groq_call
from email_bot.config import SENDER_EMAIL

class EmailBot:
    def get_email_content_from_sender(self, sender):
        content= get_email_content(sender)
        if content==None:
            return "This is a test content"
        else:
            return content

    def draft_email_reply(self, content):
        #from email_bot.openai_helper import generate_reply
        #return generate_reply(content)
        return groq_call(content)

    def send_email_reply(self, to, subject, body):
        return send_email(to, subject, body)

