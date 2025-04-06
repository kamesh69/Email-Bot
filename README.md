# Email Assistant with Robot Framework + OpenAI + Gmail API

## Features
- Reads latest email from a specific sender
- Sends email content to ChatGPT to draft a reply
- Sends the reply back via Gmail
- $env:PYTHONPATH = "."
- robot tests/email_reply_test.robot


## Setup
1. Set up Gmail API credentials and save `token.json` under `credentials/`
2. Add your OpenAI key in `config.py`
3. Install dependencies:

```bash
pip install -r requirements.txt

