"""possible to search by UserID and get a list of all images (Description) for this UserID.
 When you select an image in the list you get an overview of all comments on this image
"""
import tkinter as tk
import sqlite3
cnn = sqlite3.connect('photo_app (1).db')
crr = cnn.cursor()


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


def search_comments():
    image_id = see_comment_entry.get()
    crr.execute('select * from comments where image_id = ?', (image_id,))
    all_comments = crr.fetchall()
    print("so comment sare -----------------------------")
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




user_label = tk.Label(f1,text = 'enter user to search images: ')
user_label.pack()
user_entry = tk.Entry(f1)
user_entry.pack()
button_images = tk.Button(f1, text = 'Write id to search images',command=search_user)
button_images.pack()
images_info_label = tk.Label(f1,text = 'Here all images will show')
images_info_label.pack()


see_comment_label = tk.Label(f2, text = 'Enter image_id to see the comments')
see_comment_label.pack()
see_comment_entry = tk.Entry(f2)
see_comment_entry.pack()
button_comments= tk.Button(f2, text = 'Search image_id to see comments ', command=search_comments)
button_comments.pack()
see_comment_result_label = tk.Label(f2, text = 'Those are the comments')
see_comment_result_label.pack()

    

tk.mainloop()