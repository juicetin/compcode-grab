from dotenv import load_dotenv, find_dotenv
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import sys

# load_dotenv(find_dotenv())

def email_notify_codeword(codeword, img_path=None):
    EMAIL = os.environ.get('EMAIL')
    PWD = os.environ.get('EMAIL_PWD')

    # Start server connection
    s = smtplib.SMTP('smtp.gmail.com:587')
    recipients = ['justingling@gmail.com', 'chowshingmei@gmail.com']

    cur_date = datetime.now().strftime('%a-%b-%d')
    msg = MIMEMultipart()

    # Attach text
    text ="The codeword for today: {}, is '{}'".format(cur_date, codeword)
    text = MIMEText(text)
    msg.attach(text)

    # Attach image
    if img_path != None:
        img_data = open(img_path, 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename(img_path))
        msg.attach(image)

    # Set other message parameters
    sender = 'justingling@gmail.com'
    subject = 'Ch7 Cash Cow codeword'
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    # Send message
    s.ehlo()
    s.starttls()
    try:
        s.login(os.environ.get('EMAIL'), os.environ.get('EMAIL_PWD'))
    except AttributeError:
        print('You probably forgot to include EMAIL and EMAIL_PWD in environment vars')
        sys.exit(1)
    s.send_message(msg)
    s.quit()

    print('Message:\n{}\nsent!'.format(msg))
