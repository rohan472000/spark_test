
import email
import imaplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to, subject, email_message):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    # server.starttls()
    server.ehlo()
    server.login('insanecs03@gmail.com', 'zsqweuvfqrbczbpbkhny')

    # subject = "The Shirt you want is below $15! Now is your chance to buy!"
    # body = "Alex, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"

    # msg = f"Subject: {subject}\n\n{body}"
    print('hey mail going to be sent')
    # server.sendmail(
    #     'anand44rohan@gmail.com',
    #     'insanecs03@gmail.com'
    # )
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = "insanecs03@gmail.com"
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(email_message, "plain"))
    server.sendmail(
        'insanecs03@gmail.com',
        to, msg.as_string()
    )
    # Send the email
    # smtp_server.sendmail("insanecs03@gmail.com", to, msg.as_string())
    print('hey mail sent')
    server.quit()


# Connect to the Gmail server
# mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # smtplib.SMTP_SSL('smtp.gmail.com',465)
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("insanecs03@gmail.com", "euvfqrbczbpbkhny")
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
        send_email("insanecs03@gmail.com", subject, email_message.as_string())

    # Get the body of the email
    body = email_message.get_payload(decode=True).decode()

    # Check if the body contains "ACM", "IBM", or "ACC"
    if "ACM" in body:
        # Forward the email to the ACM team email
        send_email("acm_team@example.com", subject, email_message.as_string())
    elif "DM" in body:
        # Forward the email to the IBM team email
        send_email("ibm_team@example.com", subject, email_message.as_string())
    elif "midapps" in body:
        # Forward the email to the ACC team email
        send_email("acc_team@example.com", subject, email_message.as_string())
    elif "cmp" in body:
        # Forward the email to the ACC team email
        send_email("acc_team@example.com", subject, email_message.as_string())

# Close the connection
mail.close()
mail.logout()
# send_email('insanecs03@gmail.com', 'critical', 'yo')
