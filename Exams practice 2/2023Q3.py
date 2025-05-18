#Create a window where you can search by UserID and get a list of all 
# images (Descriptions) belonging to that UserID. When you select an image 
# from the list, you get an overview of all comments on that image.

#Create a window
#Search by userID
#Get a list of all images
#Overview of all comments on that image


images = {'img001':{'title':'sunser over mountains','description':'a sunset is casting shadows on mountains','photographer':'peter parker','date':'2024-08-01'},
          'img002':{'title':'Forest','description':'A big forest','photographer':'Max Petersen','date':'2023-05-04'},
          'img003':{'title':'City','description':'A city with tall buildings','photographer':'David Hans','date':'2022-07-08'}
          }


import tkinter as tk

def showdata():
    k = entry.get()
    if k =='q':
        label.config(text='Result: no data')
        return 
    try:    
        data = images[k]
        title = data['title']
        description = data['description']
        photographer = data['photographer']
        date = data['date']
        label.config(text=f' {title}: {description}:{date}')
    except:
        label.config(text='eRROR')



window = tk.Tk()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window,text='search data',command=showdata)
button.pack()

label = tk.Label(window, text = 'Result:')
label.pack()



tk.mainloop()


def add(a,v):
    return a+v 
add(10,20)