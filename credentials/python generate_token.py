from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os
import json

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    creds = None
    if os.path.exists('credentials/token.json'):
        with open('credentials/token.json', 'r') as token:
            try:
                creds = Credentials.from_authorized_user_info(json.load(token), SCOPES)
            except json.JSONDecodeError:
                print("❌ token.json is corrupted or empty. Deleting it...")
                os.remove('credentials/token.json')

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials/credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open('credentials/token.json', 'w') as token:
            token.write(creds.to_json())

if __name__ == '__main__':
    main()
