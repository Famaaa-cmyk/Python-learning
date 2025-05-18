import sqlite3
product_list = {'apple': 100, 'Mango': 200, 'Banana': 300, 'Grapes': 50, 'Strawberry': 75, 'Shoes': 100,}





con = sqlite3.connect('products.db')
cur = con.cursor()
con.commit()
command = """
          CREATE TABLE IF NOT EXISTS products (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name VARCHAR(100),
          price INT

)"""

cur.execute(command)
con.commit()



import tkinter as tk

window = tk.Tk()

entry = tk.Entry()
entry.pack()

def add_items():
    name = entry.get()
    price = product_list[name]
    command = f"INSERT INTO products (name,price) VALUES ('{name}','{price}')"
    cur.execute(command)
    con.commit()

def show_bill():
    command = "SELECT * FROM products"
    s = cur.execute(command)
    data = s.fetchall()
    for i in data:
        print(i)
    result.config(text=str(data))
    # use chatgpt and find how to remove data after findign total bill so you could add next titmes
    # Classes write code in form of classes to make an application with sq



add_button = tk.Button(text='Add',command = add_items)
add_button.pack()

subit_button = tk.Button(text='Subit', command = show_bill)
subit_button.pack()

result = tk.Label(text='Result')
result.pack()

tk.mainloop()

