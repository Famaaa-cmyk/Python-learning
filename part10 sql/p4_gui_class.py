import tkinter as tk # homework must make a new app but to store name age and gender, phone number
import sqlite3

class MarketApp():
    def __init__(self):
        self.connection = sqlite3.connect('store.db')
        self.cursor = self.connection.cursor()
        print('coonection and cursor are made')

    def make_table_in_data(self):
        msg = """CREATE TABLE IF NOT EXISTS store_data (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          price INT ) """
        self.cursor.execute(msg)
        self.connection.commit()
        print('Table is created')

    def add_data_in_database(self,name,price):
        msg = f"INSERT INTO store_data (name,price) VALUES ('{name}', '{price}')"
        self.cursor.execute(msg)
        self.connection.commit()
        print('data is added')
    
    def show_data_from_database(self):
        command = 'SELECT * FROM  store_data'
        data = self.cursor.execute(command)
        string = ""
        for each in data.fetchall():
            string += str(each) + '\n'
        print(string)
        return string


class GUI_app():
    def __init__(self):

        self.databse = MarketApp() # accesing databse app in self.database variable
        self.databse.make_table_in_data() # makingtable

        self.window = tk.Tk()

        self.label_prodcut = tk.Label(text='enter product name')
        self.label_prodcut.pack()
        self.product_entry = tk.Entry()
        self.product_entry.pack()


        self.label_price = tk.Label(text='enter product price')
        self.label_price.pack()
        self.price_entry = tk.Entry()
        self.price_entry.pack()


        self.button_add_data = tk.Button(text='add item',command=self.add_data_from_gui)
        self.button_add_data.pack()

        self.button_show_data = tk.Button(text='Show item',command=self.show_data_from_gui)
        self.button_show_data.pack()
        self.label_show = tk.Label(text='data is: ')
        self.label_show.pack()


    def add_data_from_gui(self):
        name = self.product_entry.get()
        price = int(self.price_entry.get())
        self.databse.add_data_in_database(name,price) # callling databse application

    def show_data_from_gui(self):
        result = self.databse.show_data_from_database()
        self.label_show.config(text = result)



app = GUI_app()
tk.mainloop()
