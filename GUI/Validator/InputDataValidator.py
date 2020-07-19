import re

from Model.DB import DB


class InputDataValidator:

    @staticmethod
    def sign_up_validator(nick, firstname, surname, email, password, r_password):
        correct_nick = True
        correct_names = True
        correct_passwords = True
        correct_email = True

        nicks = [nick[0] for nick in DB().get_data_from_db(query="SELECT nick from users")]
        if nick not in nicks:
            correct_nick = True

        if firstname.isalpha() and surname.isalpha():
            correct_names = True

        if password == r_password and re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", password):
            correct_passwords = True

        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            correct_email = True

        if all([correct_nick,  correct_names, correct_passwords, correct_email]):
            return True











