'''#Oppgave 3 
Tekstfil, linjesparart , med navn og saldo. 
Les gjennom fil og opprett objekter for alle navn(Kari og Knut) med intensivering a av saldo med beløp fra fil. 
Tekstfil, linjeseparert, med navn og saldo.
Les fil inn i dictionary 
Program ber bruker oppgi kundenavn 
Finn oppgitt navn i dictionary
Instanser objekt med oppgitt kundenavn og saldo fra Dictionary. 
Foreta innskudd/uttak med utskift av saldo etter intensivering(«pålogging»), innskudd og uttak. 
'''

#Lag tekstfil - Kunder.txt
#Les den inn i programmet 
#Og lag obejekter 
outfile = open('kunder.txt', 'w') 
outfile.write('Kari,1000\n')
outfile.write('Knut,2000\n')
outfile.close() 

#Lag klasse for kunde
class Kunde:
    def __init__(self, navn, saldo): #for name and bank balance
        self.navn = navn
        self.saldo = saldo
    def innskud(self,beløp): #How much money is added 
        self.saldo += beløp
        print(f'{self.navn} har satt inn {beløp} kr. Ny saldo er: {self.saldo} kr.')
    
    def uttak(self,beløp): #How much money is taken out
        if beløp > self.saldo:
            print(f'{self.navn} har ikke penger. Saldo er: {self.saldo} kr.')
        else:
            self.saldo -= beløp
            print(f'{self.navn} har tatt ut {beløp} kr. Ny saldo er: {self.saldo} kr.')

#Les filen inn i en dictionary 
def les_kundefil(filnavn):
    kunder = {}
    with open(filnavn, "r") as fil:
        for linje in fil:
            navn, saldo = linje.strip().split(",")
            kunder[navn] = float(saldo)
    return kunder

def hoved():
    kunder_dict = les_kundefil("kunder.txt")

    kundenavn = input("Oppgi kundenavn: ")
    if kundenavn in kunder_dict:
        kunde = Kunde(kundenavn, kunder_dict[kundenavn])
        print(f"{kunde.navn} er logget inn. Nåværende saldo: {kunde.saldo} kr.")

        # Eksempel: Foreta innskudd og uttak
        inn = float(input("Beløp å sette inn: "))
        kunde.innskudd(inn)

        ut = float(input("Beløp å ta ut: "))
        kunde.uttak(ut)
    else:
        print("Kunden finnes ikke.")

if __name__ == "__main__":
    hoved()

#Program spør om kundenavn 
#Finn navnet i dictionary
#Viser saldo med oppgitt kundenavn 
#Etter pålogging kan bruker ta innskud og uttak 