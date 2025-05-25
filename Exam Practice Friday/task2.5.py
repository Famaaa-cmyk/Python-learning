""""Moderator-slett" av kommentar på bilde. 
Velge bilde, listeboks med kommentarer, velge kommentar som skal slettes.
 Mulig å slette et bilde med alle kommentarer og likes (…«det ligger ikke cascade i databasedefinisjonen»…)
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

f3= tk.Frame(window)
f3.pack(side='left')

f4 = tk.Frame(window)
f4.pack(side='left') #For å slette kommentar 



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

def remove():
    comment_id = delete_comment_entry.get() 
    crr.execute('DELETE FROM comments where id = ?', (comment_id,))
    cnn.comit()
    print('This comment has been deleted')
    delete_comment__result_label.confif(text =f'comment with that id{comment_id} has been deleted')
 

#Enter user id  to delete a comment 
delete_comment_label = tk.Label(f4, text = 'Enter the image_ id for the comment you want to delete') #Kanskje number
delete_comment_label.pack()
delete_comment_entry = tk.Entry(f4)
delete_comment_entry.pack()
button_delete_comment = tk.Button(f4, text = 'Delete this comment', command=remove) #command
button_delete_comment.pack()
delete_comment__result_label = tk.Label(f4, text = 'This is the comment that will be deleted')
delete_comment__result_label.pack()




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