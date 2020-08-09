import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import ssl

def add_attachment(filename):
    #Opening the attachment file in read binary mode, since it is an image
    attachment = open(filename, 'rb')

    #Creating a payload object
    p = MIMEBase('application', 'octet_stream')
    p.set_payload(attachment.read())

    #Encoding Image data as base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', f'attachment; filename={filename}')

    #Attach attachment(payload) to the message
    msg.attach(p)

def send_email():

    context=ssl.create_default_context()

    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(user_email, user_password)
        smtp.sendmail(user_email, msg['To'], text)

user_email = input('Enter your email: ')
user_password = input('Enter your password: ')
recipients_email = input("Recipient's Email: ")
email_subject = input("Email Subject: ")
message = input("Email Body: ")
attachment_option = input("Add attachment? (y/n) ")

#Defining message and header
msg = MIMEMultipart()
msg['To'] = recipients_email
msg['Subject'] = email_subject

#Attaching the message to the email as plain text
msg.attach(MIMEText(message, 'plain'))

#Adding an Attachment
if attachment_option == "y" or attachment_option == "Y":
    fname = input("File name or File path of attachment? ")
    add_attachment(fname)

#Converting the whole msg into a string
text = msg.as_string()

#Sending Email
send_email()

print('[+] Email Sent!')



