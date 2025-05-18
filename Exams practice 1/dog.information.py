import tkinter as tk
dog = {
       
    'dog101':'cool and calm but hungary always',
    'dog102':'sad mostly but like to run',
    'dog103':'happy and likes to walk'

       }
window = tk.Tk()

def result():
    print('hello')
    key=ent.get()
    value = dog[key] # collection of data
    label.config(text = value)
b1=tk.Button(text='get_information', command=result)

ent = tk.Entry()

b1.pack()
ent.pack()

label = tk.Label(text='result')
label.pack()





tk.mainloop()