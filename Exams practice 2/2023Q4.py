#Create a window where it is possible to register a comment on an image (from a registered user). 
# The image is searched by ImageID, showing the description and upload date. 
# Then UserID and comment are entered and saved into the database.

#A window where you can register a comment on an image
#Image is searched by ImageID and show the decription and upload data

images = {'img001':{'title':'sunser over mountains','description':'a sunset is casting shadows on mountains','photographer':'peter parker','date':'2024-08-01'},
          'img002':{'title':'Forest','description':'A big forest','photographer':'Max Petersen','date':'2023-05-04'},
          'img003':{'title':'City','description':'A city with tall buildings','photographer':'David Hans','date':'2022-07-08'}
          }


import tkinter as tk


def enter_comment():
    comment = entry.get()
    id = entry2.get()
    images[id]['comment'] = comment
    
def showdata():
    id = entry2.get()
    label.config(text=str(images[id]))
window = tk.Tk()

entry = tk.Entry(window)
entry.pack()
entry2 = tk.Entry(window)
entry2.pack()

button = tk.Button(window,text='Enter comment',command=enter_comment)
button.pack()


button2 = tk.Button(window,text='show data',command=showdata)
button2.pack()

label = tk.Label(window, text = 'Result:')
label.pack()


tk.mainloop()