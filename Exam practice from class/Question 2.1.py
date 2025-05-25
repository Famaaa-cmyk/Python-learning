#Mulig å søke på BrukerID og få en liste over alle bilder(Beskrivelse) til denne BrukerIID’en.
# Når du velger et bilde i lista så skal du få en oversikt over alle kommentarer på ette bildet. 

bruker = {'Peter':{'bilde1':'sunset over mountains','kommentar':'a sunset is casting shadows on mountains','bilde2':'forest','kommentar':'a big pretty forest'},
          'Mia':{'bilde1':'Waves on the beach','kommentar':'Beautiful big waves on the beach','bilde2':'Sand on the beach','kommentar':'a lot of sand by the water'},
          'Erik':{'bilde1':'a cup of coffee','kommentar':'a big cup of coffee','bilde2':'city lights','kommentar':'a pretty picture of city light at nighttime'},

}

def get_comments(e):
    data = bruker[e]
    bilde1 = data['bilde1']
    kommentar = data['kommentar']
    bilde2 = data['bilde2']
    print(f'bilde1 is {bilde1} og kommentar er {kommentar}, bilde2 er {bilde2} og beskrivelsen er {kommentar}')


def get_comments(e):
    data = bruker[e]
    bilde1 = data['bilde1']
    kommentar = data['kommentar']
    bilde2 = data['bilde2']
    print(f'bilde1 is {bilde1} og kommentar er {kommentar}, bilde2 er {bilde2} og beskrivelsen er {kommentar}')


def get_comments(e):
    data = bruker[e]
    bilde1 = data['bilde1']
    kommentar = data['kommentar']
    bilde2 = data['bilde2']
    print(f'bilde1 is {bilde1} og kommentar er {kommentar}, bilde2 er {bilde2} og beskrivelsen er {kommentar}')


while True:
    e = input('enter comment to get comment, enter image, descript of or press Q to quit: ')
    if e == "q":
        break
    get_comments(e)

    