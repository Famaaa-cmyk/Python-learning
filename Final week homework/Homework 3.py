#Homework 3
#Age checker

#Ask the user for their age
#If they are under 18, print "you are a minor"
#If they are 18 or older, print "you are an adult"
#If the age is exactly 100, print a special message like "Century compleded"

age = int(input('Enter your age: '))
if age == 100:
    print('Centuray completed!')
elif age < 18:
    print('You are a minor')
else:
    print('You are an adult')
    


