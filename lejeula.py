from tkinter import *
from tkinter import ttk
import tkinter.font as font
from ClassGame import Lettre

# C'est la map qui contiendras les lettres
gameMap = [ ["A","B","G","N","I","Z","Y","I"],
			["B","H","Y","A","W","Q","U","A"],
			["H","R","D","T","P","O","V","W"],
			["L","J","G","Z","I","M","R","F"],
			["E","X","B","N","K","M","T","Y"],
			["X","T","S","L","G","Y","H","O"]]

print(len(gameMap), len(gameMap[0]))


# Initialisation de la fenetre du jeu
gameWindow = Tk()
gameWindow.title("Mot Croisé") # Titre du jeu
gameWindow.geometry("800x800") # Dimmension de la fenetre
gameWindow.configure(bg="#45458B")

# Boutton pour quitter la partie
leaveBtn = Button(gameWindow,text="Quitter",bg = "red",fg = "white",command=gameWindow.destroy)
leaveBtn.place(x=700,y=600) # emplacement forcé sur des pixel précis

# Ceci sont les font,taille de font que je vais utiliser pour les différents boutton
LetterButtonFont = font.Font(size=20) # font size pour les Lettre
LeaveButtonFont = font.Font(size=10) # font size pour le boutton quitter

# génération de la map
posy = 20 # position y du boutton de la lettre
for x in range(len(gameMap)): # on parcours la map en x
	posx = 20 # La position initiale de chaque boutton en x est donc 0 pour la premiere ligne
	for y in range(len(gameMap[0])): # On parcours la map en y
		lettre = Lettre(gameMap[x][y],gameWindow,LetterButtonFont) # on initialise les lettre grasse à la classe Lettre
		lettre.boutton.place(x=posx, y=posy) # on place le boutton de la lettre qui correspond à la position gameMap[x][y]
		posx+=100 # On incrémente de 100 la position en x pour laisser quelques pixels pour d'écart en horizontal
	posy += 115 # On incrémente de 115 la position en y pour laisser un espace de quelques pixels d'écart en vertical

gameWindow.mainloop()

