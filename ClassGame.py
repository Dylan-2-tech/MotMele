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
					["P","B","G","N","I","Z","Y","I"],
					["B","H","Y","A","W","Q","U","A"],
					["H","R","D","T","P","O","V","W"],
					["L","J","G","Z","I","M","R","F"],
					["E","X","B","N","K","W","T","Y"],
					["X","T","S","L","G","Y","H","O"],
					["V","J","A","R","O","Y","F","P"],
					["P","M","H","E","I","M","A","U"]]


		# Initialisation de la fenetre du jeu
		self.gameWindow = Tk()
		self.gameWindow.title("Mot Croisé") # Titre du jeu
		self.gameWindow.geometry("1200x650+400+250") # Dimmension de la fenetre
		self.gameWindow.minsize(width = 1200, height = 650) # Dimmension minimum de la fenetre
		self.gameWindow.maxsize(width = 1200, height = 650) # Dimmension maximale de la fenetre
		self.gameWindow.configure(bg="#45458B")

		# Boutton pour valider la sélection des lettres
		self.valideBtn = Button(self.gameWindow, text = "Valider", bg = "green", fg = "white")
		self.valideBtn.place(x = 800, y = 150)


		# Boutton pour quitter la partie
		self.leaveBtn = Button(self.gameWindow,text="Quitter",bg = "red",fg = "white",command=self.gameWindow.destroy, font = font.Font(size=15))
		self.leaveBtn.place(x = 900, y = 420) # emplacement forcé sur des pixel précis


		# Label qui affiche le mot valider
		self.MotLabel = Label(self.gameWindow,text = "")


		# Mot qui va changer au fur et à mesure de la partie
		self.mot = Mot(self.MotLabel)


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


		# Le bouton qui va deséléctionné toutes les lettres
		self.ClearLettersBtn = Button(self.gameWindow,text = "Clear", command = None)
		self.ClearLettersBtn.place(x = 800, y = 420)

		def clear(self):
			for listeLettre in self.gameMap:
				for lettre in listeLettre:
					if lettre.isClicked:
						lettre.isClicked = False
						lettre.boutton.confgure(bg = "#9090EE",activebackground="#A3A3FE")


		self.gameWindow.mainloop()


# Class des lettres
class Lettre:

	def __init__(self,lettre,x,y,game):

		self.index = -1
		self.mot = game.mot
		self.gameWindow = game.gameWindow
		self.gameMap = game.gameMap # la map où apparaissent les lettre
		self.isClicked = False # Si il est cliqué alors
		self.x = x # position x de la lettre
		self.y = y # position y de la lettre
		self.lettre = lettre
		self.boutton = Button(self.gameWindow,text="".join(lettre),
			width = 3, height = 1, font = font.Font(size=20),
			bg="#9090EE", activebackground="#A3A3FE", bd=0,
			command=self.clicked)


	def clicked(self): # méthode qui s'active quand la lettre est cliqué

		if self.isClicked: # Si la lettre est déja cliqué
			self.boutton.configure(bg = "#9090EE",activebackground="#A3A3FE")
			self.isClicked = False
			self.mot.mot = [self.mot.mot[i] for i in range(len(self.mot.mot)) if self != self.mot.mot[i]]
		
		else: # Si la lettre n'est pas encore cliqué
			# Si la lettre à droite est cliqué
			if self.x+1 < len(self.gameMap[0]) and self.gameMap[self.x+1][self.y].isClicked:
				self.mot.ajouterLettre(self)
				self.index = len(self.mot.mot)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué en haut de la lettre {self.gameMap[self.x+1][self.y].lettre}")

			# Si la lettre en bas est cliqué par rapport à celle de droite
			elif self.x-1 > 0 and self.gameMap[self.x-1][self.y].isClicked:
				self.mot.ajouterLettre(self)
				self.index = len(self.mot.mot)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué en bas de la lettre {self.gameMap[self.x-1][self.y].lettre}")

			# Si la lettre à gauche est cliqué par rapport à celle de droite 
			elif self.y+1 < len(self.gameMap) and self.gameMap[self.x][self.y+1].isClicked:
				self.mot.ajouterLettre(self)
				self.index = len(self.mot.mot)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué à gauche de la lettre {self.gameMap[self.x][self.y+1].lettre}")

			# Si la lettre à droite est cliqué par rapport à celle de gauche
			elif self.y-1 > 0 and self.gameMap[self.x][self.y-1].isClicked:
				self.mot.ajouterLettre(self)
				self.index = len(self.mot.mot)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué à droite de {self.gameMap[self.x][self.y-1].lettre}")

			else:
				self.mot.ajouterLettre(self)
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				

			# Si la lettre en haut à gauche est cliqué
			# Si la lettre en haut à droite est cliqué
			# Si la lettre en bas ç gauche est cliqué
			# Si la lettre en bas à droite est cliqué

		print(f"le mot est {self.mot.afficherMot()}")



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
		self.mot = []
		self.displayLabel = displayLabel
		self.direction = None

	def ajouterLettre(self, lettre):
		self.mot.append(lettre)

	def afficherMot(self):
		return "".join(self.mot[i].lettre for i in range(len(self.mot)))
		#self.displayLabel.set(self.mot)


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