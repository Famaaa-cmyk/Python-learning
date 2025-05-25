#Question 2

#Lag obekter av klassen Kunde 

#La bruker "logge inn" og deretter sette inn eller ta ut penger


#Les filen og lag tesktfil - saldo 

#Spør etter brukernavn og et kunde - obejt 

#La brukeren gjøre innskud eller uttak og skriv ut ny saldo 


#Class bruker

class Bruker:
    def __init__(self, navn, saldo):
        self.navn = navn
        self.saldo = saldo
    
    def innskud(self, beløp): #Deposit
        self.saldo += beløp
        print(f'{self.navn} balance after deposit is: {self.saldo}')
    
    def uttak(self, beløp): #Withdraw
        self.saldo -= beløp
        print(f'{self.navn} har tatt ut {beløp}. Ny saldo er {self.saldo}')



#Creating a empty dictionary
bruker_dict = {}
with open(r"Last_day practice/bank.txt","r") as file:
    for line in file:
        navn, bal = line.strip().split(";")
        bruker_dict[navn] = float(bal)

#Enter name to get balance
bruker_navn = input('Oppgi brukernavn for saldo: ')

if bruker_navn in bruker_dict:
    bruker = Bruker(bruker_navn, bruker_dict[bruker_navn])
    print(f'{bruker_navn} har saldo: {bruker.saldo}')

    #Deposit 
    dep = float(input('Beløp å sette inn: '))
    bruker.innskud(dep)

    #Withdraw
    wd = float(input('Beløp å ta ut: '))
    bruker.uttak(wd)

    print('Customer balance is', bruker.saldo)
else:
    print('Cusomter not found')