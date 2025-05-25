#Question 5 
#Objekt programmering for å legge til ny vare 

#Lag en produkt klasse med vnr, beskrivelse og pris 
class produkt:
    def __init__(self,vnr,beskrivelse,pris):
        self.vnr = vnr
        self.beskrivelse = beskrivelse
        self.pris = pris
    
    #Se produkter
    def vis_info(self):
        print(f'Varnenr er {self.vnr} og beskrivelse er {self.beskrivelse} og pris er {self.pris}')


    #Legge til ny produkt 
    def legge_til_produkt(self,nytt_vnr):
        self.vrn = nytt_vnr


#Et produkt 
produkt1 = produkt('123', 'Eple', '5')

#Uten nytt produkt 
produkt1.vis_info()

#Legge til nytt produkt 
produkt1.legge_til_produkt('Epler')

print('Nytt oppdatert liste')
produkt1.vis_info()
