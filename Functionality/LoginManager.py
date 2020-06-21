from Functionality.UserManager import UserManager


class LoginManager:


    @staticmethod
    def log_in():
        print('log_in')

        # if log_or_sign_up_check == 'L':
        #     login = input('Login: ')
        #     password = input('Password: ')
        #     if LoginManager.check_credentials(login, password):
        #         # ToDo: here should be method for log in
        #         pass
        # else:
        #     UserManager.create_new_user()

    # @staticmethod
    # def sign_in():


    @staticmethod
    def check_credentials(login, password):
        #print(UserManager.users.get(login)) check
        if login in UserManager.users and UserManager.users.get(login).get('password') == password:
            print('Successful')
            return True
        print("Invalid login or password. Create account if you haven't done it yet")
        # else:
        #     print("Invalid login or password. Create account if you haven't done it yet")
        #     LoginManager.login_or_register()
        #     return False



