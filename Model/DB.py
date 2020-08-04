from pprint import pprint
import mysql.connector
from mysql.connector import InterfaceError, ProgrammingError

from GUI.InfoBoxGUI import InfoBoxGUI


class DB:

    def __init__(self):

        try:
            self.toss_db = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='admin1234',
                database='tossdb')
        except (InterfaceError, ProgrammingError, AttributeError) as e:
            error = f"Probably config data are incorrect. \n\n Error: {e}"
            InfoBoxGUI().error_box(error)
        except Exception as e:
            error = f"Something went wrong during connecting with database. \n\n Error: {e}"
            InfoBoxGUI().error_box(error)



    def execute_query(self, query):
        cursor = self.toss_db.cursor()
        try:
            cursor.execute(f"{query}")
        except ProgrammingError as e:
            error = f"Check query syntax! \n\n Error: {e}"
            InfoBoxGUI.error_box(error)
        except Exception as e:
            error = f"Something is wrong... \n\n {e}"
            InfoBoxGUI().error_box(error)
        else:
            self.toss_db.commit()

    def get_data_from_db(self, query):
        cursor = self.toss_db.cursor()
        try:
            cursor.execute(f"{query}")
        except ProgrammingError as e:
            error = f"Check query syntax! \n\n Error: {e}"
            InfoBoxGUI().error_box(error)
        except Exception as e:
            error = f"Something is wrong... \n\n {e}"
            InfoBoxGUI().error_box(error)
        else:
            result = cursor.fetchall()
            return result

    # def create_toss_db(self):
    #     self.execute_query('CREATE DATABASE tossdb')


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



