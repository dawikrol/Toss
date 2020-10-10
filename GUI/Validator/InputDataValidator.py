import re
from GUI.InfoBoxGUI import InfoBoxGUI
from Model.DB import DB


class InputDataValidator:

    '''The InputDataValidator class contain methods checking user input.'''

    @staticmethod
    def sign_up_validator(nick, firstname, surname, email, password, r_password):
        correct_nick = False
        correct_names = False
        correct_password = False
        correct_r_password = False
        correct_email = False

        nicks = [nick[0] for nick in DB().get_data_from_db(query="SELECT nick from users")]
        if nick not in nicks:
            correct_nick = True
        else:
            InfoBoxGUI().info_box(message='The entered data are incorrect.\n'
                                          ' Nickname already exist in database.')

        if firstname.isalpha() and surname.isalpha():
            correct_names = True
        else:
            InfoBoxGUI().info_box(message='The entered data are incorrect.\n'
                                          'Firstname and surname cannot contain characters other than letters.')

        if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", password):
            correct_password = True
        else:
            InfoBoxGUI().info_box(message='The entered data are incorrect.\n'
                                          'The password must contain an uppercase letter, number and special character. '
                                          'Password must be longer than 6 characters')

        if password == r_password:
            correct_r_password = True
        else:
            InfoBoxGUI().info_box(message='The entered data are incorrect.\n'
                                          'The passwords are not the same.')

        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            correct_email = True
        else:
            InfoBoxGUI().info_box(message='The entered data are incorrect.\n'
                                          'Email is incorrect.')

        if all([correct_nick,  correct_names, correct_password, correct_r_password, correct_email]):
            return True

    @staticmethod
    def login_validator(login, password):
        correct_login = False
        correct_password = False

        nicks = [nick[0] for nick in DB().get_data_from_db(query="SELECT nick FROM users")]
        if login in nicks:
            correct_login = True

            password_db = DB().get_data_from_db(query=f"SELECT password FROM users WHERE nick = '{login}'")
            if password == password_db[0][0]:
                correct_password = True

        if all([correct_login, correct_password]):
            return True
        else:
            InfoBoxGUI().info_box('Login or password is incorrect.')

















