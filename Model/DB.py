from pprint import pprint
from uuid import uuid4


class DB:

    users_database = {}
    shopping_lists_database = {}
    #users_lists_database = {}


    @staticmethod
    def add_user(user):
        DB.users_database[user.nickname] = user
        pprint(DB.users_database)
        x=2

    @staticmethod
    def delete_user(user):
        if user.nickname in DB.users_database:
            DB.users_database.pop(user.nickname)
        else:
            """ Throw user not exitst"""
            print("user don't exist")

    @staticmethod
    def add_shopping_list(shopping_list):
        DB.shopping_lists_database[shopping_list.id] = shopping_list

    @staticmethod
    def delete_shopping_list(shopping_list):
        DB.shopping_lists_database.pop(shopping_list.id)

    @staticmethod
    def get_user(nickname):
        return DB.users_database.get(nickname)

    @staticmethod
    def get_shopping_lists(id):
        return DB.shopping_lists_database.get(id)