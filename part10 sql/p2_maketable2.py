# use sqlite3 instead of mysql, connect to faika.db create a table called fruitprices
# it hsould behavng  name price quantiy
# store 5 fruits data in it and print finally

import sqlite3

con = sqlite3.connect('faika.db')
cur = con.cursor()
con.commit()
command = """
          CREATE TABLE IF NOT EXISTS fruits (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name VARCHAR(100),
          price INT, 
          quantity INT

     
)"""

cur.execute(command)

con.commit()

# data entery 
f = ['apple','orange','mango','mango']
p = [100,200,300,200]
q = [10,5,14,20]

for i in range(4):
    ins = f'INSERT INTO fruits (name, price, quantity) VALUES ("{f[i]}","{p[i]}","{q[i]}")'
    cur.execute(ins)
con.commit()


cur.execute('SELECT * FROM fruits')
con.commit()

print(cur.fetchall(),'this is all data')


cur.close()
con.close()
