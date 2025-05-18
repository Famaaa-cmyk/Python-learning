#import tkinter 
# if not work you can write pip install <module_name>
#window = tkinter.Tk()


import  tkinter as tk 
window = tk.Tk()



f1 = tk.Frame(window)
f1.pack(side='bottom')



f2 = tk.Frame(window)
f2.pack(side='top')



b1 = tk.Button(f1,text='stop')
b1.grid(row=0,column=0)
l1 = tk.Label(f1,text='this is a label')
l1.grid(row=0,column=1)


b2 = tk.Button(f2,text='second frame button')
b2.pack()
l2 = tk.Label(f2,text='second frame is a label')
l2.pack()

tk.mainloop()