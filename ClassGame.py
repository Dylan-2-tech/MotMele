from tkinter import *
from tkinter import ttk
import tkinter.font as font

# Constante des différentes directions
DIAGONALE_GD = "diagonale_gauche_droite"
DIAGONALE_DG = "diagonale_droite_gauche"
LIGNE_HORIZONTAL = "ligne_horizontale"
LIGNE_VERTICAL = "ligne_verticale"




#### Fichier des class du jeu ####

# Class De la fenetre de jeu
class Jeu:

	def __init__(self):
		# C'est la map qui contiendras les lettres
		self.gameMap = [ 
					["A","B","G","N","I","Z","Y","I"],
					["B","H","Y","A","W","Q","U","A"],
					["H","R","D","T","P","O","V","W"],
					["L","J","G","Z","I","M","R","F"],
					["E","X","B","N","K","M","T","Y"],
					["X","T","S","L","G","Y","H","O"],
					["V","J","A","R","O","Y","F","P"],
					["P","M","H","E","I","M","A","U"]]


		# Initialisation de la fenetre du jeu
		self.gameWindow = Tk()
		self.gameWindow.title("Mot Croisé") # Titre du jeu
		self.gameWindow.geometry("1200x650+400+250") # Dimmension de la fenetre
		#self.gameWindow.minsize(width = 1200, height = 1000) # Dimmension minimum de la fenetre
		#self.gameWindow.maxsize(width = 1200, height = 1000) # Dimmension maximale de la fenetre
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

		self.gameWindow = gameWindow.gameWindow
		self.gameMap = gameWindow.gameMap # la map où apparaissent les lettre
		self.isCliqued = False # Si il est cliqué alors
		self.x = x # position x de la lettre
		self.y = y # position y de la lettre
		self.lettre = lettre
		self.boutton = Button(gameWindow.gameWindow,text="".join(lettre),
			width = 3, height = 1, font = font.Font(size=20),
			bg="#9090EE", activebackground="#A3A3FE", bd=0,
			command=self.clicked)


	def clicked(self): # méthode qui s'active quand la lettre est cliqué

		if self.isCliqued:
			self.boutton.configure(bg = "#9090EE",activebackground="#A3A3FE")
			self.isCliqued = False
		else:
			self.boutton.configure(bg = "red",activebackground="red")
			self.isCliqued = True



	"""
	Comment faire en sorte que le joueur ne clique pas sur des lettres impossible à choisir

	Définir une lettre choisissable:
		-si la lettre se trouve dans un périmètre de 1 dans toutes les directions 
		par rapport à la position x et y de la lettre.

	Comment trouver les lettres choisissable:

	Direction GAUCHE, HAUT, DROITE, BAS:
		- si self.x est strictement supérieure à 0 alors la lettre à gauche est en position:
			--> self.gameMap[x-1][y]
		- si self.y est strictement supérieure à 0 alors la lettre du dessus est en position:
			--> self.gameMap[x][y-1]
		- si self.x est strictement inférieur à len(self.gameMap[0])-1 alors la lettre de droite est en position:
			--> self.gameMap[x+1][y]
		- si self.y est strictement inférieur à len(self.gameMap)-1 alors la lettre du dessus est en position:
			--> self.gameMap[x][y+1]
	
	Direction en diagonale:
		- si self.x est strictement supérieure à 0 et
		  si self.y est strictement supérieure à 0 alors la lettre en haut à droite est en position:
			--> self.gameMap[x-1][y-1]
		- si self.x est strictement inférieur à len(self.gameMap[0])-1 et
		  si self.y est strictement supérieure à 0 alors la lettre en haut à gauche est en position:
		  	--> self.gameMap[x+1][y-1]
		- si self.x est strictement supérieur à 0 et
		  si self.y est strictement inférieure à len(self.gameMap)-1 
		  alors la lettre en bas à gauche est en position:
		    --> self.gameMap[x-1][y+1]
		- si self.x est strictement inférieur à len(self.gameMap[0])-1 et
		  si self.y est strictement inférieur à len(self.gameMap)-1
		  alors la lettre en bas à droite est en position:
		  	--> self.gameMap[x+1][y+1]
	"""


# Class du mot qui sera créé au fur et à mesure
class Mot:

	def __init__(self,displayLabel):
		self.mot = ""
		self.displayLabel = displayLabel
		self.direction = None

	def ajouterLettre(self, lettre):
		self.mot += lettre.lettre

	def afficherMot(self):
		self.displayLabel.set(self.mot)

	"""
	La direction du mot est diagonale gauche droite si
	on peut cliquer sur la lettre choisis et que ses coordonnées sont
	self.mot[len(mot)-1].x-1 et self.mot[len(mot)-1].y-1
	ou self.mot[len(mot)-1].x+1 et self.mot[len(mot)-1].y-1

	La direction du mot est diagonale droite gauche si
	on peut cliquer sur la lettre choisis et que ses coordonnées sont
	self.mot[len(mot)-1].x-1 et self.mot[len(mot)-1].y+1
	ou self.mot[len(mot)-1].x+1 et self.mot[len(mot)-1].y-1

	La direction du mot est verticale si
	on peut cliquer sur la lettre choisis et que ses coordonnées sont
	self.mot[len(mot)-1].x et self.mot[len(mot)-1].y-1 
	ou self.mot[len(mot)-1].x et self.mot[len(mot)-1].y+1

	La direction du mot est horizontale si
	on peut cliquer sur la lettre choisis et que ses coordonnées sont
	self.mot[len(mot)-1].x+1 et self.mot[len(mot)-1].y
	ou self.mot[len(mot)-1].x-1 et self.mot[len(mot)-1].y
	"""