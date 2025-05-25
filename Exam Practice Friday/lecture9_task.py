
"""
QUESTION (Lecture 9 Task):

You are given a text file (line-separated) that contains names and balances like:
Kari,1000
Knut,1500

TASK 1:
- Read this file and create objects for each person (e.g., Kari and Knut), 
  initializing their balance from the file.

TASK 2:
- Read the file into a dictionary with names as keys and balances as values.

TASK 3:
- Ask the user to enter a customer name (login).
- Find that name in the dictionary.
- Instantiate an object for that customer using the name and balance.
- Let the user make deposits and withdrawals.
- Print balance after login, after deposit, and after withdrawal.
"""

# ANSWER

# Sample content of file 'balances.txt':
# Kari,1000
# Knut,1500

class BankCustomer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}'s balance after deposit: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.name} has insufficient funds.")
        else:
            self.balance -= amount
            print(f"{self.name}'s balance after withdrawal: {self.balance}")

# Read balances from file into a dictionary
customer_dict = {}
with open(r"C:\Users\Bruker\OneDrive\Skrivebord\Python learning\Exam Practice Friday\balances.txt", "r") as file:
    for line in file:
        name, bal = line.strip().split(",")
        customer_dict[name] = float(bal)

# Ask user to enter customer name
customer_name = input("Enter customer name: ")

if customer_name in customer_dict:
    # Instantiate customer object
    customer = BankCustomer(customer_name, customer_dict[customer_name])
    print(f"{customer.name} logged in with balance: {customer.balance}")

    # Deposit
    dep = float(input("Enter deposit amount: "))
    customer.deposit(dep)

    # Withdraw
    wd = float(input("Enter withdrawal amount: "))
    customer.withdraw(wd)

    print('current balance is ',customer.balance)

else:
    print("Customer not found.")
    
