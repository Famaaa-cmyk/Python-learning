'''
Create a program that reads all information about dogs into a two-dimensional list. 
When reviewing the list, it should also be possible to get the client's mobile number and last name.
'''

# this code will read data
import json
file = open('Exam prac\dog.json')
data = json.load(file)
print(data)

for dog in data:
    print(f'Dog name is {dog[0]} its owner name is {dog[3]}')