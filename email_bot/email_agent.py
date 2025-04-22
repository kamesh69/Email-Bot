from datetime import datetime, timedelta
import email
from email_bot.gmail_service import connect_imap, connect_smtp
from email_bot.email_utils import parse_email_body, get_sender, generate_reply, send_email
from email.utils import parsedate_tz, mktime_tz

def process_unread_emails():
    print("Processing Unread Emails..")
    mail = connect_imap()  # IMAP connection to check inbox
    mail.select("inbox")  # Select inbox folder
    print("IMAP connection established and inbox selected.")

    # Search for unread emails in the last 15 minutes
    date_15_minutes_ago = (datetime.now() - timedelta(minutes=15)).strftime('%d-%b-%Y')
    print(f"Searching for unread emails since: {date_15_minutes_ago}")

    # Search for unread emails from the last 15 minutes
    result, data = mail.search(None, f'(UNSEEN SINCE {date_15_minutes_ago})')
    if result != 'OK':
        print(f"Error searching emails: {result}")
        return
    
    email_ids = data[0].split()  # List of email IDs
    print(f"Found {len(email_ids)} unread email(s). Email IDs: {email_ids}")

    if not email_ids:
        print("No unread emails found.")
        return

    # Loop through each email
    for e_id in email_ids:
        print(f"Fetching email ID: {e_id}")
        res, msg_data = mail.fetch(e_id, "(RFC822)")
        if res != 'OK':
            print(f"Error fetching email ID {e_id}: {res}")
            continue
        
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        print(f"Processing email from: {msg['From']}")
        sender = get_sender(msg)  # Extract sender email
        body = parse_email_body(msg)  # Extract the email body

        # Print the extracted sender and body for debugging
        print(f"Sender: {sender}")
        print(f"Email Body: {body[:100]}...")  # Print only first 100 chars of the body for readability

        # If a sender and body are found, generate a reply and send it
        if sender and body:
            print(f"Generating reply for email from {sender}.")
            reply = generate_reply(body)  # Generate a reply using AI
            print(f"Generated reply: {reply[:100]}...")  # Preview first 100 chars of reply
            send_email("Re: Your recent email", reply, sender)
            print(f"Replied to {sender}")
        else:
            print(f"No valid sender or body found for email ID {e_id}. Skipping email.")
    mail.logout()
if __name__ == "__main__":
    process_unread_emails()