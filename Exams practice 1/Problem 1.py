'''
Case: Create a program that reads all dog information into a two-dimensional dictionary.
It should print out the dog's name and breed of a specific dog
when the program asks the user to enter the DogID. The program should run as long as the users want to.
'''

dog = {
       
    'dog101':{'name':'tom','breed':'bulldog'},
    'dog102':{'name':'siren','breed':'poodle'},
    'dog103':{'name': 'Happy', 'breed': 'Pitbull'}, 
    'dog104':{'name': 'Tony', 'breed': 'Labrador'}, 
    'dog105':{'name': 'Tommy', 'breed': 'Husky'}

       }


# import json
# file = open('filename.json')
# json.read(file)
loop ='yes'
while loop == 'yes':
    user = input('Please enter the dogID:')
    name = dog[user]['name']
    breed = dog[user]['breed']
    print('The name of the dog is',name)
    print('The breed of the dog is', breed)
    loop = input('Do you want to run th program again? yes|no:')
    
print('program eneded...')



