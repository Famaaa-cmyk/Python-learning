outfile = open('kunder.txt', 'w') 
outfile.write('Kari,1000\n')
outfile.write('Knut,2000\n')
outfile.close()
# Kundeklasse
class Kunde:
    def __init__(self, navn, saldo):
        self.navn = navn
        self.saldo = saldo

    def innskudd(self, beløp):
        self.saldo += beløp
        print(f"{self.navn} har satt inn {beløp} kr. Ny saldo: {self.saldo} kr.")

    def uttak(self, beløp):
        if beløp > self.saldo:
            print(f"{self.navn} har ikke nok penger. Saldo: {self.saldo} kr.")
        else:
            self.saldo -= beløp
            print(f"{self.navn} har tatt ut {beløp} kr. Ny saldo: {self.saldo} kr.")

# Leser fil inn i dictionary
def les_kundefil(filnavn):
    kunder = {}
    with open(filnavn, "r") as fil:
        for linje in fil:
            navn, saldo = linje.strip().split(",")
            kunder[navn] = float(saldo)
    return kunder

# Hovedprogram
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
