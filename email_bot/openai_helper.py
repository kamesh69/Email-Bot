# email_bot/openai_helper.py

import openai

from email_bot.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_reply(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who drafts email replies."},
            {"role": "user", "content": f"Draft a reply to the following email:\n\n{prompt}"}
        ]
    )
    return response.choices[0].message.content.strip()
