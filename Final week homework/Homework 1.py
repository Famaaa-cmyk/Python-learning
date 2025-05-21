#Homework 1: Even or Odd

#Ask the user to enter a number 
#If the number is odd, check if it also greater than 100 and mention ihat too. 

#Write a program that asks the user to enter the number
#If it's even, print"Even number"
#If it's odd, print "odd numbers"
#If it's odd and greater than 100, print "odd and big number!"

enter_number = int(input('Enter a number: '))
if enter_number % 2 == 0:
    print('This is a even number')
else:
  
    if enter_number >= 100:
        print('This is Odd and big number!')


    