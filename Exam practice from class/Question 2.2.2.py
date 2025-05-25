#-	Mulig å søke på BildID og alle kommentarene til dette bildet vises i en listeboks.
#  Når en velger en kommentar i lista får en informasjon om brukeren som har lagt inn kommentaren (fornavn og etternavn).


bilder = {'img001':{'first comment': 'This is very nice', 'User': 'Peter Olav', 'second comment': 'This is beautiful', 'User': 'Mia Hans'}, 
         'img002':{'first comment': 'This is a nice photograf', 'User': 'Spencer Reid', 'second comment': 'This is very beautiful', 'User': 'Emily Hanna'},  
          }

import tkinter as tk 

#Search with photoID
#def enter_id():
    

window = tk.Tk()

entry = tk.Entry(window)
entry.pack() #For photoID



label = tk.Label(window, text = 'Kommentarer:')
label.pack() #To show comments

#Should be possible to search up PhotoID and get all comments on that images into a gui box
#HWhen the user chooses a comments in the list it should be possible to get all information aboth the user that commentet (first and last name)

#Sarch button after you enter PhotoID

#Label showing the comments 

#Button to get user information 
#Label to show the information 

tk.mainloop()