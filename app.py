import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Dummy Account'
email['to'] = 'dummyaccount2d@gmail.com'
email['subject'] = 'I\'m a python master'

email.set_content(html.substitute({'name': 'lalala'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'password')
    smtp.send_message(email)
    print('all good')