product_list = {'apple': 100, 'Mango': 200, 'Banana': 300, 'Grapes': 50, 'Strawberry': 75, 'Shoes': 100,}
names = []
prices = []
import tkinter as tk

window = tk.Tk()

entry = tk.Entry()
entry.pack()

def add_items():
    name = entry.get()
    price = product_list[name]
    names.append(name)
    prices.append(price)
    print('item is added',name)

def show_bill():
    s = ''
    for i in range (len(names)):
        s = s + f'{names[i]} \t \t {prices[i]} \n'
    total_bill = 'total: ' + str ( sum(prices) )
    s = s + total_bill
    result.config(text=s)
    print('reset go for order')



add_button = tk.Button(text='Add',command = add_items)
add_button.pack()

subit_button = tk.Button(text='Subit', command = show_bill)
subit_button.pack()

result = tk.Label(text='Result')
result.pack()

tk.mainloop()

