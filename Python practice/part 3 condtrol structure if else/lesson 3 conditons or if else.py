# if true run code 1 , else run code 2
temperature = input('enter temperature value: ')
temperature = int( temperature )
if temperature < 10:
    print('turn on Heater')
    print('abc')
else:
    print('Turn off Heater')
print('program ended')



### please make a simplete program that will if age less then 13 then you are kid
### else if age is less than 20 you are a teen ager
## else you are adult
age = 19
if age < 13:
    print('You are a child')
else:
    if age < 20:
        print('You are a teenger')
    else:
        print('You are a adult')



age = 19
if age < 13:
    print('You are a child')
elif age < 20:
    print('You are a teenger')
else:
    print('You are a adult')


## usign elif if marks less than 50 print fail, elif marks > 50 and marks <80 grade B, elif marks >= 80 and marks <90 grade A, elif marks greater or equal to 90 and less than 100 A+
marks = input('Enter your marks: ')
marks = float(marks)
if marks < 50:
    print('Fail')
elif marks >= 50 and marks < 80:
    print('Grade B')
elif marks >=80 and marks <90:
    print('Grade A')
elif marks >=90 and marks < 100:
    print('A+')
else:
    print('invalid keep values between 0 to 100')
