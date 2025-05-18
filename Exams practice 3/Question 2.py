'''Create a program that reads all information about customers into a two-dimensional dictionary and
prints out First Name (Fornavn) and Last Name (Etternavn) for a specific customer when the
program prompts the user to enter the Mobile Number (Mobilnr). The program should run as long as
the user wants.'''

file = open('Exams practice 3/customer.txt')

lst = []
for line in file.readlines():
    line = line.strip()
    lst.append(line.split(','))
print(lst)

d = {}
for line in lst:
    fname = line[1]
    lname = line[2]
    add = line[3]
    post = line[4]
    phone = line[0]

    d[phone] = {'address':add,'firt_name':fname,'lname':lname,}

print('------------------')

x = input('enter the phone number:')
print(d[x])