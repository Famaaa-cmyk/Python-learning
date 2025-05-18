import tkinter as tk
import sqlite3

conn = sqlite3.connect('Rental2.db')
cor = conn.cursor()


Command = """
CREATE TABLE IF NOT EXISTS rent (
    reg_number VARCHAR(50) PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status VARCHAR(20),
    total_cost DECIMAL(10, 2)
)"""
cor.execute(Command)
conn.commit()

def data_entry(reg,name,start_date,end_date,status,total_cost):
    command = f"""
    INSERT INTO rent (
        reg_number,
        customer_name,
        start_date,
        end_date,
        status,
        total_cost
    ) VALUES (
        '{reg}',
        '{name}',
        '{start_date}',
        '{end_date}',
        '{status}',
        {total_cost}
        );
        """
    return command


def save_data():
   reg_value = reg.get()
   name = customer_name.get()
   start = start_date.get()
   end = end_date.get()
   sta = status.get()
   total = total_cost.get()
   cnt = data_entry(reg_value, name, start, end, sta, total)
   cor.execute(cnt)
   conn.commit()
   res.config(text = f'Data {reg_value} saved')

def load_data():
    reg_value2 = reg_2.get()
    ans = show_data(reg_value2)
    res.config(text = f'the data {ans}')



def show_data(reg):
    command = "SELECT * FROM rent"
    s = cor.execute(command)
    data = s.fetchall()
    for i in data:
        if i [0] == reg: 
            return i 
    return f'no value found for {reg}'
    













window = tk.Tk()
f1 = tk.Frame(window)
f1.pack(side='left')
f2 = tk.Frame(window)
f2.pack(side='right')
reg_label = tk.Label(f1, text = 'Reg number')
reg_label.pack()
reg = tk.Entry(f1) 
reg.pack()
customer_label = tk.Label(f1, text = 'Customer name')
customer_label.pack()
customer_name = tk.Entry(f1)
customer_name.pack()
start_label = tk.Label(f1, text = 'Start date')
start_label.pack()
start_date = tk.Entry(f1)
start_date.pack()
end_label = tk.Label(f1, text = 'End date')
end_label.pack()
end_date = tk.Entry(f1)
end_date.pack()
status_label = tk.Label(f1, text = 'Status')
status_label.pack()
status = tk.Entry(f1)
status.pack()
total_label = tk.Label(f1, text = 'Total cost')
total_label.pack()
total_cost = tk.Entry(f1)
total_cost.pack()

button = tk.Button(f1, text = 'Enter data', command = save_data )
button.pack()

reg_label_2 = tk.Label(f2, text = 'Enter reg number to get data')
reg_label_2.pack()
reg_2 = tk.Entry(f2)
reg_2.pack()

button_2 = tk.Button(f2, text = 'Get data', command = load_data)
button_2.pack()

res = tk.Label(f2,text = '')
res.pack()

tk.mainloop()
