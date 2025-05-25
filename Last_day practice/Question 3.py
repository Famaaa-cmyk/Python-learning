#Question 3
#Vising av bilder og kommentarer

#Import sqlite3 og koble til databasen 
import sqlite3
conn = sqlite3.connect(r"C:\Users\Bruker\OneDrive\Skrivebord\Python learning\Last_day practice\bilder.db")
cursor = conn.cursor()


#Finner bilde etter user_ID (bilde_id)
bilde_id = input('Skriv inn bilde_Id for å finne bilde: ')


#Viser bildebeskrivelse i en liste
cursor.execute('SELECT * FROM bilder where bilde_id = ?', (bilde_id))
beskrivelse = cursor.fetchall()
if beskrivelse:
    print(f'Dette er beskrivelse av bildet {bilde_id}: {beskrivelse[0]}')
else:
    print('Bildet ikke funnet')
    exit()


#Når en kommentar velges, vis bruker som har kommentert

#Mulightet til å slette vlagt kommentar

#Mulighter til å slette bilder og alle kommentarer/likes manuelt 

conn.close()