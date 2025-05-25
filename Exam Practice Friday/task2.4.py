"""•	Mulig å søke på BildeID og alle kommentarer til dette bildet vises i en listeboks. 
Når en velger en kommentar i lista får en informasjon om brukeren som har lagt inn kommentaren (fornavn og etternavn)
"""
import tkinter as tk
import sqlite3
cnn = sqlite3.connect('photo_app (1).db')
crr = cnn.cursor() # koble mot databasen


#Search up a spesific user and get a list of all images (desctptions) for that userID

def search_user(): #Search up a spesific user 
    identitity = user_entry.get()
    crr.execute('select * from users where id = ?', (identitity,))
    all_users = crr.fetchall()
    print(all_users)

    crr.execute('select * from images where user_id = ?', (identitity,))
    all_images = crr.fetchall()
    print(all_images)
    s = ''
    for image in all_images:
        s = s + str(image) + '\n'
    images_info_label.config(text = s)

    return all_users

#Få opp kommentarer til et bilde 
def search_comments():
    image_id = see_comment_entry.get()
    crr.execute('select * from comments where image_id = ?', (image_id,))
    all_comments = crr.fetchall()
    print("so comments are -----------------------------")
    print(all_comments)
    s = '' 
    
    for c in all_comments:
        s = s + str(c) + '\n'

    see_comment_result_label.config(text = s)



window = tk.Tk()

f1 = tk.Frame(window)
f1.pack(side='left')

f2 = tk.Frame(window)
f2.pack(side='left')

f3= tk.Frame(window)
f3.pack(side='left')



#Skriv inn bruker for å søke på bilde
user_label = tk.Label(f1,text = 'enter user to search images: ')
user_label.pack()
user_entry = tk.Entry(f1)
user_entry.pack()
button_images = tk.Button(f1, text = 'Write id to search images',command=search_user)
button_images.pack()
images_info_label = tk.Label(f1,text = 'Here all images will show')
images_info_label.pack()

#Skriv in bildeID for å se kommentarer
see_comment_label = tk.Label(f2, text = 'Enter image_id to see the comments')
see_comment_label.pack()
see_comment_entry = tk.Entry(f2)
see_comment_entry.pack()
button_comments= tk.Button(f2, text = 'Search image_id to see comments ', command=search_comments)
button_comments.pack()
see_comment_result_label = tk.Label(f2, text = 'Those are the comments')
see_comment_result_label.pack()



#For å søke på bruker med hvilken kommentar de har skrevet.
def get_user_by_comment():
    comment_id = search_user_by_comments_entry.get()
    crr.execute('select * from comments where id = ?',(comment_id,))
    data = crr.fetchall()
    user_id =data[0][2]
    user_id = str(user_id)
    print(data)
    crr.execute('select * from users where id = ?',(user_id,))
    name = crr.fetchall()
    print(name)
    s= ''
    for n in name :
        s = s + str(n) + '\n'
    see_user_comments_result.config(text = s)

 
search_user_by_comments_label = tk.Label(f3, text = 'Search user by comments')
search_user_by_comments_label.pack()
search_user_by_comments_entry = tk.Entry(f3)
search_user_by_comments_entry.pack()
button_user_comments = tk.Button(f3, text= 'Get user by comments', command = get_user_by_comment)
button_user_comments.pack()
see_user_comments_result = tk.Label(f3, text = ' Those are the users by comments')
see_user_comments_result.pack()




tk.mainloop()