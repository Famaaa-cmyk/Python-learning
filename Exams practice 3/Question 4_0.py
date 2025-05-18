'''Create a program to complete a rental. The user enters the car's Registration Number and the
information about the rental is displayed. 
The user enters the remaining details of the rental and
confirms that the rental is completed and the database is updated.'''



class Rental:
    def __init__(self,reg_number,customer_name,start_date): 
        self.reg_number = reg_number 
        self.customer_name = customer_name
        self.start_date = start_date
        self.end_date = None
        self.total_cost = None 
        self.status= 'Rented'
    def display(self):
        print(f'''the car has registration {self.reg_number} and customer name is {self.customer_name} and 
start date is {self.start_date} and the end date is {self.end_date} and the total cost is {self.total_cost} 
and it's status is {self.status}''')
    def complete(self):
        self.end_date = input('Enter the end date (format:yyyy-mm-dd):')
        self.total_cost = input('Enter the total cost: ')
        self.status='Free'

    #def store_data(self):
        #database[self.reg_number] = {'cusotmer_name':self.customer_name, 'start_date':self.start_date,'end_date':self.end_date,'total_cost':self.total_cost,'status':self.status}
        




car1 = Rental('car111','faika','2025-05-10')
car1.display()
car1.complete()
car1.display()