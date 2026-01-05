import csv
import os
import smtplib
from datetime import datetime
from email.message import EmailMessage

def send_email(occasion, custom_message):
    # These are pulled safely from GitHub Secrets
    SENDER_EMAIL = "your-email@gmail.com" 
    APP_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    
    msg = EmailMessage()
    msg['Subject'] = f"Diet Reminder: {occasion}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = SENDER_EMAIL
    msg.set_content(custom_message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

# 1. Get today's date in YYYY-MM-DD format
today = datetime.now().strftime("%Y-%m-%d")

# 2. Check the CSV
if os.path.exists('festivals.csv'):
    with open('festivals.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == today:
                print(f"Match found for {row['Occasion']}! Sending email...")
                send_email(row['Occasion'], row['Message'])
else:
    print("CSV file not found!")