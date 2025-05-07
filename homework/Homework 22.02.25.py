#Homework 22.02.25

#1.Write a function to check if a number is divisle by 5.
def anyname(num):
    if num%5 == 0:
        return 'it is divisible'
    else:
        return 'not divisible'


#2.Create a function that prints all even numbers from 1 to 100.
def fun2():
    num=1
    while num >=1 and num <=100:
        if num %2 == 0:
            print( 'Even',num )
        else:
            print( 'Odd', num )
        num = num + 1

#3.Write a function that takes two numbers and returns their sum.
#Alternative 1

def fun3(num1,num2):
    return num1+num2

#4.Make a functions that prints 'Hello, World' five times.
def helooo():
    for _ in range(5):
        print('Hello,world!')
