import mysql.connector
from mysql.connector import InterfaceError, ProgrammingError
from GUI.InfoBoxGUI import InfoBoxGUI
from Model.User import User


class DB:

    def __init__(self):
        # TODO: eliminate keeping DB credentials in code
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
            InfoBoxGUI().error_box(error)
        except Exception as e:
            error = f"Something is wrong... \n\n {e}"
            InfoBoxGUI().error_box(error)
        else:
            self.toss_db.commit()
        cursor.close()

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

    def get_user_from_db(self, nick):
        query = f"SELECT * FROM users WHERE nick=\'{nick}\'"
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
            user_id = result[0][0]
            nick = result[0][1]
            firstname = result[0][2]
            surname = result[0][3]
            email = result[0][4]
            return User(user_id, nick, firstname, surname, email)


