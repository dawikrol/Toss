import random

class RegistrationManager:

    users_id_list = []

    @staticmethod
    def sign_in():
        print('si')


    @staticmethod
    def generate_user_id():
        random_num = random.randint(10000, 99999)
        if random_num not in RegistrationManager.users_id_list:
            RegistrationManager.users_id_list.append(random_num)
            return random_num
        else:
            RegistrationManager.generate_user_id()




