#Homework 28.02.25
#1.Making a dictionary called students where keys are student names and values are their ages. 
#Add three students to the dictionary

students = {
    'Peter':'21',
    'Alex': '25',
    'Adam':'19',
}

print(students)


#2.Accessing the dictionary, capitals.
#Print France.

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}

print(capitals['France'])

#3.Using loop to get values and print them:
#A loop to print all students names.

students = {'umair':'abc','arfa':10,'ali':50}
for a,b in students.items():
    print(a)
    

#4.Loop on country and print codes if it is even. 
#Print only the country codes that are even numbers from the dictionary of county codes.
country_codes = {
    1: "USA",
    44: "UK",
    33: "France",
    86: "China",
    91: "India"
}

for code,country in country_codes.items():
    if code %2==0:
        print(f'{code} is a even number for {country}')

#5.If fruits contain a letter, Print it
#Check if each fruit contains the letter 'a'. If its does print the fruit name. 

fruits = ['Apple', 'Banana', 'Cherry', 'Grape', 'Kiwi']
for f in fruits:
   if 'a' in f:
       print(f)



#6.Print only the username from database of username and passwords. 
#Create a dictionary called users where the keys are username and the values are passwords. 
#Then write a loop to print only the username. 

username = {'Ola':'abc','Anne':10,'Ida':50}
for a,b in username.items():
    print(a)
    