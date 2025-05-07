#Homework 25-02-25
#1.Create a list named fruits with some fruits and print the list. 
fruit = ['Apple','Banana', 'Cherry', 'Mango','Grapes']
print(fruit)

#2. Access and print the first and last elements of the following list using both positive and negative indexing 
colors = ['Red', 'Blue', 'Green', ' Yellow', 'Purple']
print('The first value is', colors[0] )
print('The last value is', colors [4] )
print('The last value is', colors [-1] )


#3. Insert 'Orange' at the second position (index 1) in the following list, then print the updated list.
fruit.insert(1,'Orange')
print(fruit)

#4. Append "Black" to the end of the given list then print the updated list.
colors.append('Black')
print(colors)

#5.Genereate and print all possible cf the following fruits and colors list.
fruit = ['Apple','Banana', 'Cherry', 'Mango','Grapes']
colors = ['Red', 'Blue', 'Green', ' Yellow', 'Purple']
for f in fruit:
    for c in colors:
        print(f,c)
