import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(to_email: str, subject: str, body: str):
    """
    Sends an email using Gmail SMTP.
    """

    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        print("Email credentials not configured.")
        return

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = EMAIL_ADDRESS
    message["To"] = to_email
    message.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(message)

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Failed to send email: {e}")