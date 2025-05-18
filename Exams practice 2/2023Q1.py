'''
Create a program that reads all information about users
into a two dimentional list and print out USERID, last name, email by groing through the list'''

# reading
# two dimentional list
# printing
# going throught the list (means loop)


users = [['ID101','John', 'Peter', 'peter_01@gmail.com'],['ID105','apple','orange','apple@orange.coom'],['ID102','John', 'David', 'david_02@gmail.com'], ['ID103','John', 'Max', 'Max_03@gmail.com'] ]

for user in users:
    id = user[0]
    last_name = user[2]
    email = user[3]
    print(f'ID is {id} email is {email} and last name is {last_name}')