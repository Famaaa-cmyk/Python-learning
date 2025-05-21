file = open('Exams practice 3/customer2.txt')


lst = []
for line in file.readlines():
    line = line.strip()
    lst.append(line.split(','))
print(lst)

d = {}
for line in lst:
    phone = line[0]
    first_name = line[1]
    last_name = line[2]
    jobb = line[3]
    
    d[phone] = {'First_name':first_name,'Last_name':last_name,}

print('----------------')

loop = True
while loop == True:
    x = input('Enter the phone number of the customer: ')
    print(d[x])
    q = input('enter quit if you want to end program:')
    if q =='quit':
        loop = False