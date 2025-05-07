import tkinter as tk
class MyGUI:
    def __init__(self,size,database):
        self.database = database

        self.root = tk.Tk()
        self.root.geometry(size)

        self.label1 = tk.Label(self.root,text='name of fruit')
        self.label1.pack()
   
        ## please addd entry for writitng fruit name
        self.ent  = tk.Entry(self.root)
        self.ent.pack()


        self.label2 = tk.Label(self.root, text='how much kgs')
        self.label2.pack()
                            

        self.ent2  = tk.Entry(self.root)
        self.ent2.pack()


        self.but = tk.Button(self.root, text='Calculate',command=self.fun)
        self.but.pack()

        self.label3 = tk.Label(self.root,text='total:')
        self.label3.pack()


        tk.mainloop()


    def fun(self):
        print('helloww')
        name = self.ent.get()
        try:
            price = self.database[name]
            quantiry = int(self.ent2.get())

            result = str(price*quantiry)
            self.label3.config(text=f'result :{result}')
        except:
            self.label3.config(text=f'ERROR')
        

if __name__ == "__main__":
    d = {'apple':10,'mango':15,'orange':20,'grapes':30}
    my_gui = MyGUI('700x350',d)
