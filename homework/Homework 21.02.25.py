#1.Write a for loop to print numbers from 1 to 20 using the range function
for num_2 in range(1,21):
    print(num_2)

#2.Write a while loop to print all even numbers between 50 and 100.
num=50
while num >=50 and num <=100:
    if num %2 == 0:
        print( 'Even',num )
    else:
        print( 'Odd',num )
    num = num + 1

#3.Create a list of colors and use a for loop to print only those that containt the letter 'e'.
colors = ['red', 'blue', 'green', 'purple', 'pink', 'black', 'yellow']
for color in colors:
    if 'e' in color:
        print(color)

#4.Write a loop that prints the multiplication table of 5 up to 10 times.
nums = (5*1,5*2,5*3,5*4,5*5,5*6,5*7,5*8,5*9,5*10)
for num_5 in nums:
    print(num_5)
### anohter way
for i in range(51):
    if i%5 ==0:
        print('abc',i)

#5.Create a list of random numbers and use a for loop to find and
#print the largest number in the list. 
numbers = [10,35,85,99,130,586,6843,69436836,93606,66265,53,5]

final_number = 0
for current_number in numbers:
    if current_number > final_number:
        final_number = current_number
    
