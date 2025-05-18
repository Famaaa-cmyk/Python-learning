'''Create a program to complete a rental. The user enters the car's Registration Number and the
information about the rental is displayed. The user enters the remaining details of the rental and
confirms that the rental is completed and the database is updated.'''
Rental_database = {
    "CAR001": {
        "customer_name": "Ali Khan",
        "start_date": "2025-05-01",
        "end_date": None,
        "total_cost": None,
        "status": "Active"
    },
    "CAR002": {
        "customer_name": "Sara Ahmed",
        "start_date": "2025-05-02",
        "end_date": None,
        "total_cost": None,
        "status": "Active"
    },
    "CAR003": {
        "customer_name": "Usman Tariq",
        "start_date": "2025-05-03",
        "end_date": None,
        "total_cost": None,
        "status": "Active"
    },
    "CAR004": {
        "customer_name": "Ayesha Riaz",
        "start_date": "2025-05-04",
        "end_date": None,
        "total_cost": None,
        "status": "Active"
    },
    "CAR005": {
        "customer_name": "Zainab Malik",
        "start_date": "2025-05-05",
        "end_date": None,
        "total_cost": None,
        "status": "Active"
    }
}

def display(databse,reg_number):
    for a,b in databse[reg_number].items():
        print(a,b)

def complete(database,reg_number):
    end_date = input('Enter the end date (format:yyyy-mm-dd):')
    total_cost = input('Enter the total cost: ')
    status='Free'

    database[reg_number]['end_date'] = end_date
    database[reg_number]['total_cost'] = total_cost
    database[reg_number]['status'] = status
    

while True:
    x = input('do you want to display/complete/quit:')
    
    if x =='display':
        reg = input('enter registration number:')
        display(Rental_database,reg)
    elif x == 'complete':
        reg = input('enter registration number:')
        complete(Rental_database,reg)
    elif x=='quit':
        break
    else:
        print('invalid value')

print(Rental_database)