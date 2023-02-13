import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import imaplib
import email


def send_email(to, subject, email_message):
    # Set up the email server
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login("insanecs03@gmail.com", "Rohan@Rohit47")

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = "your_email@gmail.com"
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(email_message, "plain"))

    # Send the email
    smtp_server.sendmail("insanecs03@gmail.com", to, msg.as_string())

    # Close the connection
    smtp_server.quit()


# Connect to the Gmail server
mail = smtplib.SMTP_SSL('smtp.gmail.com',465)
mail.login("insanecs03@gmail.com", "Rohan@Rohit47")
mail.select("inbox")

# Search for new emails
status, email_ids = mail.search(None, "UNSEEN")
email_ids = email_ids[0].split()

# Loop through all emails
for email_id in email_ids:
    # Get the email
    status, email_data = mail.fetch(email_id, "(RFC822)")
    email_message = email.message_from_bytes(email_data[0][1])

    # Get the subject of the email
    subject = email_message["subject"]

    # Check if the subject contains "critical", "major", or "minor"
    if "critical" in subject.lower():
        # Forward the email to the dev team email
        send_email("anand00rohit@gmail.com", subject, email_message.as_string())
    elif "major" in subject.lower():
        # Forward the email to the dev team email
        send_email("anand00rohit@gmail.com", subject, email_message.as_string())
    elif "minor" in subject.lower():
        # Forward the email to the dev team email
        send_email("anand00rohit@gmail.com", subject, email_message.as_string())

# Close the connection
mail.close()
mail.logout()
