import smtplib
from email.message import EmailMessage
from GUI.InfoBoxGUI import InfoBoxGUI
from Model.DB import DB


class MessageManager:

    def __init__(self, id_list, name_of_list, products, number, prices, cost, members, cost_per_member):
        self.id_list = id_list
        self.name_of_list = name_of_list
        self.products = products
        self.number = number
        self.prices = prices
        self.cost = cost
        self.members = members
        self.cost_per_member = cost_per_member
        self.prepare_list_to_send()

    def start(self):
        self.prepare_list_to_send()

    def prepare_list_to_send(self):
        subject = f'List:  {self.name_of_list} completed!'
        query = f"SELECT owner FROM lists WHERE list_id={self.id_list}"
        owner = DB().get_data_from_db(query)
        body = f'Hello!\n\n The list {self.name_of_list} has been completed.\n Details of list below:\n\n' \
               f'Products|   Number   |   Price\n\n'
        for item, num, price in zip(self.products, self.number, self.prices):
            body += f'{item}|   {num}|   {price}\n'
        body += f'\n\nSum up: {self.cost}.\n You should return {self.cost_per_member} PLN to {owner[0][0]} who is owner the list.'
        emails = []
        for user in self.members:
            query = f"SELECT email FROM users WHERE userid = {user[0]}"
            emails.append(DB().get_data_from_db(query)[0][0])
        self.send_list(subject, body, emails)

    def send_list(self, subject, body, emails):
        for email in emails:
            self.send_msg(subject, body, email)

    def send_msg(self, subject, body, recipient):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = 'menagerlists@gmail.com'
        msg['To'] = f'{recipient}'
        msg.set_content(f'{body}')
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('menagerlists@gmail.com', 'ovoneL09')
                smtp.send_message(msg)
        except Exception as e:
            print(e)
            print(msg['To'])
            error = f"Mail could not be sent. \n Check internet connection. \n\n Error: {e}"
            InfoBoxGUI().error_box(error)

