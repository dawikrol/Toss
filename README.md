# Toss

My first training project. Toss is shopping list that you can share with your friends. The main goals this project was:
- understanding OOP in Python
- using database in Python project
- createing application in Python

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
host='localhost',
user='root',
passwd='admin1234',
database='tossdb')
```

I know that we should keep credentials in this wasy. It was my first project ;)). 

In this project I use standard SQL querying. Now I would use SQLAlchemy and ORM to do this in more Python way. 
Of course I would use password hashing too.


### Functionality

- Sign in new users
- Log in users
- Creat shopping list which can be share with other users
- Edit existing list
- Send mails to members of list
