#Question 1
#Du har en tekstfil med bruker saldo og navn 
#Be om brukernavn
#Hent saldo 
#Skriv den ut 

#Class bruker
class Bruker:
    def __init__(self, navn, saldo):
        self.navn = navn
        self.saldo = saldo
    




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

else:
    print('Cusomter not found')

