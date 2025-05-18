'''Create a program that reads all information about the images into a 
two-dimensional dictionary and prints out Description and Photographer for a specific 
image when the program prompts the user to enter an ImageID. The program should run as long as the user wants.
'''
images = {'img001':{'title':'sunser over mountains','description':'a sunset is casting shadows on mountains','photographer':'peter parker','date':'2024-08-01'},
          'img002':{'title':'Forest','description':'A big forest','photographer':'Max Petersen','date':'2023-05-04'},
          'img003':{'title':'City','description':'A city with tall buildings','photographer':'David Hans','date':'2022-07-08'}
          }


while True: 
    k = input('Enter the Image ID: or press Q to Quit:')
    if k =='q':
        break
    data = images[k]
    title = data['title']
    description = data['description']
    photographer = data['photographer']
    date = data['date']
    print(f'The title of the image is {title} The description is {description} The date is {date}')

