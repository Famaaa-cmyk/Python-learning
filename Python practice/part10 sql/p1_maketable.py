# import mysql.connector

# # how to connect to database
# conn = mysql.connector.connect(
#     host='127.0.0.1',
#     user='root',
#     password='1234',
#     database=''
# )

import sqlite3 

conn = sqlite3.connect('mydata.db')

# how to make table 
command = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    email VARCHAR(100)
)"""

cursor = conn.cursor()
cursor.execute(command)
conn.commit()
# how to save data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John','apple') )
conn.commit()

data1 = "INSERT INTO users (name, email) VALUES ('faika','faika123213@gmail.com')"
cursor.execute(data1)
conn.commit()


# how to access data
see = 'SELECT * FROM users'
cursor.execute(see)
print(cursor.fetchall())


# close connection
cursor.close()
conn.close()
