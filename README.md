# Toss

My first training project. Toss is shopping list that you can share with your friends. The main goals this project was:
- understanding OOP in Python
- using database in Python project
- creating application in Python

### Table of contents
* [Technologies](#Technologies)
* [Database](#Databse)
* [Functionality](#Functionality)


### Technologies

Python(3.7)

   Main libraries: tkinter
  
MySQL(8.0)


### Database

Database configuration is required:
Model -> DB.py

```
MYSQL_HOSTNAME = 'localhost'
MYSQL_USER = os.environ.get('DB_USER')
MYSQL_PASSWORD = os.environ.get('DB_PASS')
MYSQL_DATABASE = 'tossdb'
```


In this project I use standard SQL querying. Now I would use SQLAlchemy and ORM to do this in more Python way. 
Of course I would use password hashing too.

Database script to create database is available in DB_scripts


### Functionality

- Sign in new users
- Log in users
- Creat shopping list which can be share with other users
- Edit existing list
- Send mails to members of list


Main menu:


![image](https://user-images.githubusercontent.com/63808220/114876403-9317da00-9dfe-11eb-9b83-9c8a08565182.png)

