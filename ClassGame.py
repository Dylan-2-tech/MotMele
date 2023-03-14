from tkinter import *
from tkinter import ttk
import tkinter.font as font

#### Fichier des class du jeu ####

# Class De la fenetre de jeu
class Jeu:

	def __init__(self):
		# C'est la map qui contiendras les lettres
		self.gameMap = [ ["A","B","G","N","I","Z","Y","I"],
					["B","H","Y","A","W","Q","U","A"],
					["H","R","D","T","P","O","V","W"],
					["L","J","G","Z","I","M","R","F"],
					["E","X","B","N","K","M","T","Y"],
					["X","T","S","L","G","Y","H","O"]]


		# Initialisation de la fenetre du jeu
		self.gameWindow = Tk()
		self.gameWindow.title("Mot Croisé") # Titre du jeu
		self.gameWindow.geometry("1000x500+400+250") # Dimmension de la fenetre
		self.gameWindow.minsize(width = 1000, height = 500) # Dimmension minimum de la fenetre
		self.gameWindow.maxsize(width = 1000, height = 500) # Dimmension maximale de la fenetre
		self.gameWindow.configure(bg="#45458B")

		# Boutton pour valider la sélection des lettres
		self.valideBtn = Button(self.gameWindow, text = "Valider", bg = "green", fg = "white")
		self.valideBtn.place(x = 800, y = 150)


		# Boutton pour quitter la partie
		self.leaveBtn = Button(self.gameWindow,text="Quitter",bg = "red",fg = "white",command=self.gameWindow.destroy, font = font.Font(size=15))
		self.leaveBtn.place(x = 900, y = 420) # emplacement forcé sur des pixel précis


		# génération de la map
		posy = 40 # position y du boutton de la lettre
		for x in range(len(self.gameMap)): # on parcours la map en x
			posx = 40 # La position initiale de chaque boutton en x est donc 0 pour la premiere ligne
			for y in range(len(self.gameMap[0])): # On parcours la map en y
				lettre = Lettre(self.gameMap[x][y],x,y,self) # on initialise les lettre grâce à la classe Lettre
				lettre.boutton.place(x=posx, y=posy) # on place le boutton de la lettre qui correspond à la position gameMap[x][y]
				self.gameMap[x][y] = lettre
				posx+=75 # On incrémente de 100 la position en x pour laisser quelques pixels pour d'écart en horizontal
			posy += 75 # On incrémente de 115 la position en y pour laisser un espace de quelques pixels d'écart en vertical


		self.gameWindow.mainloop()


# Class des lettres
class Lettre:

	def __init__(self,lettre,x,y,gameWindow):
		self.gameMap = gameWindow.gameMap
		self.isCliqued = False
		self.x = x
		self.y = y
		self.lettre = lettre
		self.boutton = Button(gameWindow.gameWindow,text="".join(lettre),
			width = 3, height = 1, font = font.Font(size=20),
			bg="#9090EE", activebackground="#A3A3FE", bd=0,
			command=self.clicked)

	def clicked(self):
		self.boutton.configure(bg = "red",activebackground="red")
		if self.isCliqued:
			print(f"La lettre {self.gameMap[self.x][self.y].lettre} est déjà selectionné")
		else:
			print(f"La lettre {self.lettre} a été cliqué à la position ({self.x},{self.y})")
		self.isCliqued = True



# Class du mot qui sera créé au fur et à mesure
class Mot:

	def __init__(self,displayLabel):
		self.mot = ""
		self.displayLabel = displayLabel

	def ajouterLettre(self, lettre):
		self.lettres += lettre

	def afficherMot(self):
		self.displayLabel.set(self.mot)