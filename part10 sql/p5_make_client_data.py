#Make a new app to store name, age, gender and phone number

import tkinter as tk
import sqlite3

class UserApp():
    def __init__(self):
        self.connection = sqlite3.connect('user.db')
        self.cursor = self.connection.cursor()
        
    def user_in_databse(self):
        inf = """CREATE TABLE IF NOT EXISTS user_data   (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT,
        age INT,
        gender TEXT,
        nr INT )"""
        self.cursor.execute(inf)
        self.connection.commit()
        
    def adding_data_in_base(self,name,age,gender,nr):
        inf = f"INSERT INTO user_data (name,age,gender,nr) VALUES ('{name}', '{age}','{gender}','{nr}')"
        self.cursor.execute(inf)
        self.connection.commit()

    def show_data(self):
        commad = 'SELECT * FROM user_data'
        data = self.cursor.execute(commad)
        string = ""
        for each in data.fetchall():
            string += str(each) + '\n'
            print(string)
        return string
        
class GUI_app():
    def __init__(self):
        self.database = UserApp()
        self.database.user_in_databse()
        
        self.window = tk.Tk()

        self.label_name = tk.Label(text='Enter the name')
        self.label_name.pack()
        self.name_entry = tk.Entry()
        self.name_entry.pack()

        self.label_age = tk.Label(text='Enter the age')
        self.label_age.pack()
        self.age_entry = tk.Entry()
        self.age_entry.pack()

        self.label_gender = tk.Label(text='Enter the gender')
        self.label_gender.pack()
        self.gender_entry = tk.Entry()
        self.gender_entry.pack()
        
        self.label_nr = tk.Label(text='Enter the phone number')
        self.label_nr.pack()
        self.nr_entry = tk.Entry()
        self.nr_entry.pack()

        self.button_adding_data = tk.Button(text='Add user', command=self.add_data)
        self.button_adding_data.pack()

        self.label_add =  tk.Label(text='')
        self.label_add.pack()

        self.button_showing_data = tk.Button(text='Show user information', command=self.show_user_data)
        self.button_showing_data.pack()
        self.label_show = tk.Label(text='The user information is: ')
        self.label_show.pack()

    def add_data(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        gender = self.gender_entry.get()
        nr = int(self.nr_entry.get())
        self.database.adding_data_in_base(name,age,gender,nr)
        self.label_add.config(text=f'data for {name} is added')
    
    def show_user_data(self):
        result = self.database.show_data()
        self.label_show.config(text = result)

app = GUI_app()
tk.mainloop()        
        