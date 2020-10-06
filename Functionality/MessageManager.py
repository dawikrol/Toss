import smtplib
from email.message import EmailMessage

from Model.User import User


class MessageManager:

    def __init__(self):
        pass


    def send_list(self, title, items):
        body = f'{title}\n\n'
        for i in items:
            body += f'{i[0]} :      {i[1]}\n'
        msg = EmailMessage()
        msg['Subject'] = 'Your list!'
        msg['From'] = 'menagerlists@gmail.com'
        msg['To'] = f'{User.current_logged.email_address}'
        msg.set_content(f'{body}')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('menagerlists@gmail.com', 'ovoneL09')

            # first is sender
            smtp.send_message(msg)

#MessageManager()
