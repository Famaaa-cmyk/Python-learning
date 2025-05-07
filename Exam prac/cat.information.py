import tkinter as tk

cat = {
    'Cat1':'Lifespan is 12-14 years',
    'Cat2': 'Lifespan is 11-12 years',
    'Cat3': 'Lifespan is 8-10 years'

    }

window=tk.Tk()

def results():
    print('hello')
    key = ent.get()
    data = cat[key]
    label.config(text=data)

    #Make a button 
b1 = tk.Button(text='Results', command=results)
b1.pack()

    #Make a entry 
ent = tk.Entry()
ent.pack()

    #Make a label 
label = tk.Label()
label.pack()


tk.mainloop()