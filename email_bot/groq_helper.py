import os
from groq import Groq
from email_bot.config import GROQ_API_KEY

def groq_call(prompt):

    client = Groq(
        api_key=GROQ_API_KEY,  # This is the default and can be omitted
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant who drafts email replies."},
            {"role": "user", "content": f"Draft a reply to the following email:\n\n{prompt}"}
        ],
        model="llama3-8b-8192",
    )
    return (chat_completion.choices[0].message.content)
