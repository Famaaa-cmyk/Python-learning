'''Create a program where you search by the car's Registration Number and get a list of all rentals for
that car, sorted by rental date. When a rental is selected from the list, you get information about who
rented the car (Mobile Number, First Name, and Last Name).
'''




file = open('Exams practice 3/car_rental.txt')

lst = []
for line in file.readlines():
    line = line.strip()
    line = line.split(',')
    lst.append(line)

print(lst)

reg = input('Enter the registration number: ')

details = {}
for line in lst:
    if reg ==line[0]:
        date = line[1]
        fname = line[2]
        phone = line[4]

        #print(f'date of rent is {date} name of person is {fname} phone number of the person is {phone}')
        details[date] = {'FNAME':fname,'LNAME':phone}
        
print(details)
sorted_details = sorted(details.items())
print(sorted_details)
print('program ended')