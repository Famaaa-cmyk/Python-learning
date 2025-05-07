# load the text file and save it as a 2 dimentional list

# open fil name
file = open('Exam prac\dog.txt', 'r')

## readlines to data vairbale
dogs = file.readlines()

# apply a for loop on data and split data with ,
new_list = []
for dog in dogs:
    dog = dog.strip()
    data = dog.split(',')
    new_list.append(data)

# append it to a list
print(new_list)


