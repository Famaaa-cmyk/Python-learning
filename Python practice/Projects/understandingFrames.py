import tkinter as tk
window = tk.Tk()
top=tk.Frame()
buttom=tk.Frame()
label1=tk.Label(top,text='label 1 ')
label2 = tk.Label(top,text='label 2')
label3 = tk.Label(buttom,text='label 3')
label4 = tk.Label(buttom,text='label 4')

label1.pack(side='top')
label2.pack(side='top')
label3.pack(side='left')
label4.pack(side='left')

top.pack(side='top')
buttom.pack(side='top')
window.mainloop()