'''Create a program that reads all information about the cars
into a two0dimentional list and prints out Registration number, brand, and start date by going through the list'''

import json 
file = open(r'Exams practice 3\cars.json')
cars = json.load(file)


print('The cars are:',cars)

file.close()



