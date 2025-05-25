#Question 5
#Objekt programmering of endring av epost

#Bruk objekter for å:
#Legge til nytt produkt ved hjelp av klasse

#Legge til et nytt bildeobjekt og vise informasjon 

#Endre epost til en bruker og skriv ut oppdaert epost 

#Lag en bruker klasse med id, navn og email
class bruker:
    def __init__(self,id,navn,email):
        self.id = id
        self.navn = navn
        self.email = email
    
    def vis_info (self):
        print(f'Navn: {self.navn} og ID er {self.id} og email er {self.email}')
    



#Lag en produkt klasse med vnr, beskrivelse og pris 


#Opprett objekter for hver av disse 

#Vise ny email 

    
#Endre epost for brukeren 
    def endre_email(self, ny_email):
        self.email = ny_email
        
        #En bruker 
bruker1 = bruker('Kari', 'Petersen', 'kari@eksempel.no')
        #Før endring 
print('Før ennbdring')
bruker1.vis_info()
        #Endre epost
bruker1.endre_email('kari@nybruker.no')
        #Skriv ut oppdatert brukerinfo
print('Ny oppdatert brukerinfo')
bruker1.vis_info()
