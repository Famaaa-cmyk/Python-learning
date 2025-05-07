#Homework 20.02.25 

#Program 1
#Program that asks the user to enter their age.
#convert the input to an integer.

#If age is 18 or older, print the statment "you are eligble to vote
#Otherwise print "you are not eligible to vote
age = input('Enter your age ')
age = int( age )
if age >=18:
    print('You are eligble to vote')
else:
    if age < 18:
        print('You are not eligble to vote')


#Program 2
#if-elif-else logic
#write a program that asks the user to enter a number
#convert the inout to an integer and classify it as followes.
        
#Greater than 100: "large number"
#Between 50and 100(inclusive): "medium number"
#Less than 50: 'Small number'

nums = input('Enter a number: ')
nums = float(nums)
if nums > 100:
    print('Large number')
elif nums >=50 and nums <=100:
    print('Medium number')
elif nums <50:
    print('Small number')
#Note on the program. Does not do small numbers
#Does not print all numbers. 

    
#Program 3 
#Input conversion and i-elif condions:
#A program that asks the user to enter a temperature in Celsius.
    
#Convert the input to a float and classify the temperature as follos.
#Above 30°C: 'Hot'
#Between 15°C and 30°C(inclusive): 'Warm'
#Below 15°C: 'Cold'

temp = input ('Enter the temperature in Celsius: ')
temp = float(temp)

if temp >30:
    print('Hot')
elif temp >=15 and temp <=30:
    print('Warm')
elif temp < 15:
    print('Cold')

#Note - Does not do cold 

