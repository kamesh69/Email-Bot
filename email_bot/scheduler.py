import schedule
import time
from email_bot.email_agent import process_unread_emails

schedule.every(1).minutes.do(process_unread_emails)

print("📩 Email Agent running every 15 minutes...")
while True:
    schedule.run_pending()
    time.sleep(1)