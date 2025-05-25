"""possible to search by UserID and get a list of all images (Description) for this UserID.
 When you select an image in the list you get an overview of all comments on this image
"""
import sqlite3
cnn = sqlite3.connect('new_data_images.db')
crr = cnn.cursor()

def search_all_users():
    crr.execute('select * from users')
    all_users = crr.fetchall()
    print(all_users)
    return all_users


def search_user(user_id):
    crr.execute('select * from users where id = ?', user_id)
    all_users = crr.fetchall()
    print(all_users)
    return all_users


def all_images(user_id):
    crr.execute('select * from images where id = ?', user_id)
    all_users = crr.fetchall()
    print(all_users)
    return all_users
def description(user_id): 
    user_id = str(user_id)
    crr.execute('select * from images where id = ?', user_id)
    data = crr.fetchall()
    print(data[0][2],'description')

def all_comments():
    pass

search_all_users()
search_user('5')
all_images('5')
description(5)


