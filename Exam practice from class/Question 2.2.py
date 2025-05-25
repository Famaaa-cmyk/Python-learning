#-	Mulig å søke på BildID og alle kommentarene til dette bildet vises i en listeboks.
#  Når en velger en kommentar i lista får en informasjon om brukeren som har lagt inn kommentaren (fornavn og etternavn).

bruker = {'Peter':{'bilde1':'sunset over mountains','kommentar':'a sunset is casting shadows on mountains','bilde2':'forest','kommentar':'a big pretty forest'},
          'Mia':{'bilde1':'Waves on the beach','kommentar':'Beautiful big waves on the beach','bilde2':'Sand on the beach','kommentar':'a lot of sand by the water'},
          'Erik':{'bilde1':'a cup of coffee','kommentar':'a big cup of coffee','bilde2':'city lights','kommentar':'a pretty picture of city light at nighttime'},
          }

import tkinter as tk 

def show_kom():
    e = entry.get()
    if e == 'q':
        label.config(text='Result: no data')
        return
    try:
        data = bruker[e]
        bilde1 = data['bilde1']
        kommentar = data['kommentar']
        bilde2 = data['bilde2']
        label.config(text=f'{bilde1}: {kommentar}, {bilde2}: {kommentar}')
    except:
        label.config(text='Error')

window = tk.Tk()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window,text='search BildeID',command=show_kom)
button.pack()

label = tk.Label(window, text = 'Kommentarer:')
label.pack()



tk.mainloop()
def add(a,v):
    return a+v 
add(10,20)
    #print(f'bilde1 is {bilde1} og kommentar er {kommentar}, bilde2 er {bilde2} og beskrivelsen er {kommentar}')

#Denne skal bare vise kommentaren på ett bilde når man skriver bildeID
#Så det blir "skriv inn bildeId" også viser den kommentarenr til det bildet. 