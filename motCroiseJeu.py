from tkinter import *
from tkinter import ttk
import tkinter.font as font
from ClassGame import Lettre





# Ceci sont les font,taille de font que je vais utiliser pour les différents boutton
LetterButtonFont = font.Font(size=20) # font size pour les Lettre
LeaveButtonFont = font.Font(size=15) # font size pour le boutton quitter



# Boutton pour valider la sélection des lettres
valideBtn = Button(gameWindow, text = "Valider", bg = "green", fg = "white",command=afficherMot)
valideBtn.place(x = 800, y = 150)


# Boutton pour quitter la partie
leaveBtn = Button(gameWindow,text="Quitter",bg = "red",fg = "white",command=gameWindow.destroy)
leaveBtn.place(x = 900, y = 420) # emplacement forcé sur des pixel précis

# génération de la map
posy = 40 # position y du boutton de la lettre
for x in range(len(gameMap)): # on parcours la map en x
	posx = 40 # La position initiale de chaque boutton en x est donc 0 pour la premiere ligne
	for y in range(len(gameMap[0])): # On parcours la map en y
		lettre = Lettre(gameMap[x][y],gameWindow,LetterButtonFont,mot) # on initialise les lettre grâce à la classe Lettre
		lettre.boutton.place(x=posx, y=posy) # on place le boutton de la lettre qui correspond à la position gameMap[x][y]
		posx+=75 # On incrémente de 100 la position en x pour laisser quelques pixels pour d'écart en horizontal
	posy += 75 # On incrémente de 115 la position en y pour laisser un espace de quelques pixels d'écart en vertical

gameWindow.mainloop()