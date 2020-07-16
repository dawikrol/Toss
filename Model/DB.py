from pprint import pprint
import mysql.connector


class DB:

    def __init__(self):
        self.toss_db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='admin1234'
        )
        #self.create_toss_db()

    def execute_query(self, query):
        cursor = self.toss_db.cursor()
        cursor.execute('USE tossdb')
        cursor.execute(f"{query}")
        self.toss_db.commit()

    def create_toss_db(self):
        self.execute_query('CREATE DATABASE tossdb')

    # def create_users_table(self):
    #     query = '''
    #         CREATE TABLE users (
    #         userid INTEGER(10) AUTO_INCREMENT PRIMARY KEY,
    #         nick VARCHAR(30),
    #         firstname VARCHAR(30),
    #         surname VARCHAR(30),
    #         email VARCHAR(30),
    #         password VARCHAR(30)
    #         )'''
    #     self.execute_query(query)

    def add_user(self, user):
        query = f"INSERT INTO users VALUES (NULL, '{user.nickname}', '{user.firstname}', '{user.surname}', '{user.email_address}', '{user.password}')"
        self.execute_query(query)
    # @staticmethod
    # def delete_user(user):
    #     if user.nickname in DB.users_database:
    #         DB.users_database.pop(user.nickname)
    #     else:
    #         """ Throw user not exitst"""
    #         print("user don't exist")
    #
    # @staticmethod
    # def add_shopping_list(shopping_list):
    #     DB.shopping_lists_database[shopping_list.id] = shopping_list
    #
    # @staticmethod
    # def delete_shopping_list(shopping_list):
    #     DB.shopping_lists_database.pop(shopping_list.id)
    #
    # @staticmethod
    # def get_user(nickname):
    #     return DB.users_database.get(nickname)
    #
    # @staticmethod
    # def get_shopping_lists(id):
    #     return DB.shopping_lists_database.get(id)



