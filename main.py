import csv
import os
import smtplib
from datetime import datetime
from email.message import EmailMessage

def send_email(occasion, custom_message):
    SENDER_EMAIL = "cam.iphone170124@gmail.com"
    RECEIVER_EMAIL = "27.prachisingh@gmail.com" # Double check this is correct!
    
    # .strip() removes any accidental spaces from your GitHub Secret
    APP_PASSWORD = str(os.environ.get('EMAIL_PASSWORD')).strip()
    
    msg = EmailMessage()
    msg['Subject'] = f"Diet Reminder: {occasion}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(custom_message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
        print(f"Email sent successfully to {RECEIVER_EMAIL}")

# Get today's date in YYYY-MM-DD format
today = datetime.now().strftime("%Y-%m-%d")

if os.path.exists('festivals.csv'):
    with open('festivals.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == today:
                print(f"Match found for {row['Occasion']}! Sending email...")
                send_email(row['Occasion'], row['Message'])
else:
    print("CSV file not found!")