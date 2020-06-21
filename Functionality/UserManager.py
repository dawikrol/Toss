from Functionality.RegistrationManager import RegistrationManager
from Model.DB import DB
from Model.User import User



class UserManager:

    # dictionary contain users, in the future it will be change on database
    users = {'Dawid': {
                    'user_id': 'Dawid',
                    'firtsname': 'd',
                    'surname': 'd',
                    'email': 'd@d',
                    'password': 'Dawid',
                }}

    @staticmethod
    def create_new_user(nick, firstname, surname, email, password ):
        user = User(nick, firstname, surname, email, password)
        DB.add_user(user)
        # user_id = RegistrationManager.generate_user_id()
        # new_user = User(nick, firstname, surname, email, password, user_id)
        # UserManager.add_user_to_database(new_user)

        #return new_user


    @staticmethod
    def add_user_to_database(new_user):
        '''In the future database will be implemented instead list of dictionary'''
        user = \
            {
                new_user.nickname: {
                    'user_id': new_user.user_id,
                    'firtsname': new_user.firstname,
                    'surname': new_user.surname,
                    'email': new_user.email_address,
                    'password': new_user.password,
                }
            }
        UserManager.users.update(user)
        print(user)





