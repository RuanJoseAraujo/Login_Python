import sqlite3 

banco = sqlite3.connect('login.db')

cursor = banco.cursor()

# cursor.execute("CREATE TABLE users (id integer, name text, birthdate text, email text)")

def showUsers():
    cursor.execute("select * from users")
    print(cursor.fetchall())

