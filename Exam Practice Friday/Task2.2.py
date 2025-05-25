"""possible to search by UserID and get a list of all images (Description) for this UserID.
 When you select an image in the list you get an overview of all comments on this image
"""
import sqlite3
cnn = sqlite3.connect('photo_app (1).db')
crr = cnn.cursor()

def search_all_users(): #Get all users 
    crr.execute('select * from users')
    all_users = crr.fetchall()
    print(all_users)
    return all_users

def search_user(user_id): #Search up a spesific user 
    crr.execute('select * from users where id = ?', user_id)
    all_users = crr.fetchall()
    print(all_users)
    return all_users

def all_images(user_id): #Search up a spesific images in the database 
    crr.execute('select * from images where id = ?', user_id)
    all_users = crr.fetchall()
    print(all_users)
    return all_users

def description(user_id): #Search up a spesific comment
    user_id = str(user_id)
    crr.execute('select * from images where id = ?', user_id)
    data = crr.fetchall()
    print(data[0][2],'description')

def all_comments(): #Gets all comments
    crr.execute('select * from comments')
    all_comments = crr.fetchall()
    print(all_comments)
    return all_comments





search_all_users()
search_user ('8')
all_images('5')
description(5)
all_comments()
