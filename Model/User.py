import random


class User:

    current_logged = None

    def __init__(self, nickname, firstname, surname, email_address, password):
        self.nickname = nickname
        self.firstname = firstname
        self.surname = surname
        self.email_address = email_address
        self.password = password


    # def gen_user_id(self):
    #     User.user_id_list = []
    #     a = random.randint(10000, 99999)
    #     if a not in User.user_id_list:
    #         self.user_id = a
    #         User.user_id_list.append(a)
    #     else:
    #         self.gen_user_id()

    # def get_user(self):
    #     user = \
    #         {
    #             'Nick: ':self.nickname,
    #             'Name: ':self.firstname,
    #             'Surname: ':self.surname,
    #             'Email: ':self.email_address,
    #             'Password: ':self.password
    #             'User_id: ':self.user_id
    #
    #         }
    #     print('*'*30)
    #     print('You create new user:')
    #     for k, v in user.items():
    #         print(k, v)





