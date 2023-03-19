from tkinter import *
from tkinter import ttk
import tkinter.font as font


#### Fichier des class du jeu ####

# Class de la fenetre de jeu
class Jeu(Tk):

	def __init__(self):
		super().__init__()

		self.gameMap = [ 
					["P","O","U","R","I","Z","Y","I"],
					["B","H","S","A","W","Q","U","A"],
					["H","R","I","T","P","O","V","W"],
					["L","J","R","R","I","M","R","F"],
					["E","X","I","N","K","W","T","Y"],
					["X","O","S","L","G","Y","H","O"],
					["V","J","A","R","O","Y","F","P"],
					["P","M","H","E","I","M","A","U"]
					]
		# Méthode qui renvoie la map du jeu
		def get_map(self):
			return self.gameMap

		# Initialisation de la fenetre du jeu
		self.title("Mot Mélé") # Titre du jeu
		self.geometry("1200x650+400+250") # Dimmension de la fenetre
		self.minsize(width = 1200, height = 650) # Dimmension minimum de la fenetre
		self.maxsize(width = 1200, height = 650) # Dimmension maximale de la fenetre
		self.configure(bg="#45458B")

		# Boutton pour valider la sélection des lettres
		self.valideBtn = Button(self, text = "Valider", bg = "green", fg = "white", command = lambda:valider(self))
		self.valideBtn.place(x = 800, y = 150)

		# Boutton pour quitter la partie
		self.leaveBtn = Button(self,text="Quitter",bg = "red",fg = "white",command=self.destroy, font = font.Font(size=15))
		self.leaveBtn.place(x = 900, y = 420) # emplacement forcé sur des pixel précis

		# Label qui affiche le mot valider
		self.MotLabel = Label(self,bg = "#45458B",font = font.Font(size=20),fg = "white")
		self.MotLabel.place(x = 700, y = 300)

		# Mot qui va changer au fur et à mesure de la partie
		self.mot = Mot()

		# Méthode Valider
		def valider(self):
			self.MotLabel.configure(text = self.mot.mot_correct())


		# génération de la map des lettres
		posy = 40 # position y du boutton de la lettre
		for x in range(len(self.gameMap)): # on parcours la map en x
			posx = 40 # La position initiale de chaque boutton en x est donc 0 pour la premiere ligne
			for y in range(len(self.gameMap[0])): # On parcours la map en y
				lettre = Lettre(self.gameMap[x][y],x,y,self) # on initialise les lettre grâce à la classe Lettre
				lettre.boutton.place(x=posx, y=posy) # on place le boutton de la lettre qui correspond à la position gameMap[x][y]
				self.gameMap[x][y] = lettre
				posx+=75 # On incrémente de 100 la position en x pour laisser quelques pixels pour d'écart en horizontal
			posy += 75 # On incrémente de 115 la position en y pour laisser un espace de quelques pixels d'écart en vertical

		self.mainloop() # Affichage de la fenetre

		"""
		
		# Le bouton qui va deséléctionné toutes les lettres
		self.ClearLettersBtn = Button(self.gameWindow,text = "Clear", command = None)
		self.ClearLettersBtn.place(x = 800, y = 420)


		# Fonction Valider
		def Valider(self):
			print(self.mot)


		# Fonction qui nettoie les lettres sélectionner mais pas validé
		def clear(self):
			for listeLettre in self.gameMap:
				for lettre in listeLettre:
					if lettre.isClicked and not lettre.valide:
						lettre.isClicked = False
						lettre.boutton.confgure(bg = "#9090EE",activebackground="#A3A3FE")

		def check_Word(self):
			i = 0
			trouve = false
			while (not trouve and i < len(self.listeMots)):
				trouve = listeMots[i] == self.mot.text.afficher_Text()
				i += 1

			if trouve:
				print("Mot trouve")
			else:
				print("Mot pas trouve")

		"""


# Class des lettres
class Lettre:

	def __init__(self,lettre,x,y,game):

		self.mot = game.mot
		self.isClicked = False # Si il est cliqué alors
		self.x = x # position x de la lettre
		self.y = y # position y de la lettre
		self.lettre = lettre
		self.boutton = Button(game,text="".join(lettre),
			width = 3, height = 1, font = font.Font(size=20),
			bg="#9090EE", activebackground="#A3A3FE", bd=0,
			command=self.clicked)
	
	def clicked(self): # méthode qui s'active quand la lettre est cliqué

		if self.isClicked: # Si la lettre est déja cliqué
			self.boutton.configure(bg = "#9090EE",activebackground="#A3A3FE") # On remet une couleur par défaut 
			self.isClicked = False # Elle devient plus cliqué
			self.mot.text = [self.mot.text[i] for i in range(len(self.mot.text)) if self != self.mot.text[i]] # On retire la lettre du mot
		
		else: # Si la lettre n'est pas encore cliqué
			self.boutton.configure(bg = "red",activebackground="red") # On change sa couleur pour dire qu'elle est cliqué
			self.isClicked = True # Elle devient cliqué
			self.mot.ajouter_Lettre(self) # On l'ajoute au mot
 	
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

	def __init__(self):
		self.text = []

	def __str__(self):
		return "".join(self.text[i].lettre for i in range(len(self.text)))

	def ajouter_Lettre(self, lettre):
		self.text.append(lettre)

	def mot_correct(self):
		"""Renvoie True si chaque lettre du mot suivent la même direction"""

		if len(self.text) > 1:

			startX = self.text[0].x+1 # Position x pour comparer les positions avec self.text[i].x
			startY = self.text[0].y+1 # Position y pour comparer les positions avec self.text[i].y
			indLetter = 1 # Indice de départ pour comparais les lettres
			wellFormed = False # Booléen qui va confirmé si le mot est mal formé

			# Si toutes les lettres sont positionné horizontalement
			while not wellFormed and indLetter < len(self.text):
				wellFormed = self.text[indLetter].x == startX and self.text[indLetter].y == startY
				if indLetter == len(self.text)-1:
					return f"mot horizontal {indLetter}"
				else:
					startX += 1
					indLetter += 1

			if wellFormed:
				return "Mot horizontal"
			else:
				return "mot pas horizontale"

		else:
			return "Pas un mot"


		"""
		# Si le mot est bien formé horizontalement
		# On réinitialise les valeurs de comparaisons
		startX = self.text[0].x+1 # Position x pour comparer les positions avec self.text[i].x
		indLetter = 1 # Indice de départ pour comparais les lettres

		# Si toutes les lettres sont positionné verticalement
		while not wellFormed and indLetter < len(self.text): 
			if self.text[indLetter].y == startY: # Si le mot est bien formé verticalement
				wellFormed = True
				return True
			else:
				startY += 1
				indLetter += 1
		# On réinitialise les valeurs de comparaisons
		startX = self.text[0].x+1 # Position x pour comparer les positions avec self.text[i].x
		startY = self.text[0].y+1 # Position y pour comparer les positions avec self.text[i].y
		indLetter = 1 # Indice de départ pour comparais les lettres

		# Si toutes les lettres sont positionné en diagonale d'en haut à gauche à en bas à droite
		while not wellFormed and indLetter < len(self.text):
			if self.text[indLetter].x == startX and self.text[indLetter].y == startY: # Si le mot est bien formé horizontalement alors on renvoie True
				wellFormed = True
				return True
			else:
				startX += 1
				startY += 1
				indLetter += 1
		# On réinitialise les valeurs de comparaisons
		startX = self.text[0].x-1 # Position x pour comparer les positions avec self.text[i].x
		startY = self.text[0].y+1 # Position y pour comparer les positions avec self.text[i].y
		indLetter = 1 # Indice de départ pour comparais les lettres

		# Si les lettres sont positionné toutes en diagonale d'en haut à droite à en bas à gauche
		while not wellFormed and indLetter < len(self.text):
			if self.text[indLetter].x == startX and self.text[indLetter].y == startY: # Si le mot est bien formé horizontalement alors on renvoie True
				wellFormed = True
				return True
			else:
				startX -= 1
				startY += 1
				indLetter += 1
		
		return wellFormed
		"""
		

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


			# Si la lettre à droite est cliqué
			if self.x+1 < len(self.gameMap[0]) and self.gameMap[self.x+1][self.y].isClicked:
				self.mot.ajouter_Lettre(self)
				self.index = len(self.mot.text)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué en haut de la lettre {self.gameMap[self.x+1][self.y].lettre}")

			# Si la lettre en bas est cliqué par rapport à celle de droite
			elif self.x-1 > 0 and self.gameMap[self.x-1][self.y].isClicked:
				self.mot.ajouter_Lettre(self)
				self.index = len(self.mot.text)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué en bas de la lettre {self.gameMap[self.x-1][self.y].lettre}")

			# Si la lettre à gauche est cliqué par rapport à celle de droite 
			elif self.y+1 < len(self.gameMap) and self.gameMap[self.x][self.y+1].isClicked:
				self.mot.ajouter_Lettre(self)
				self.index = len(self.mot.text)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué à gauche de la lettre {self.gameMap[self.x][self.y+1].lettre}")

			# Si la lettre à droite est cliqué par rapport à celle de gauche
			elif self.y-1 > 0 and self.gameMap[self.x][self.y-1].isClicked:
				self.mot.ajouter_Lettre(self)
				self.index = len(self.mot.text)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué à droite de {self.gameMap[self.x][self.y-1].lettre}")

			else:
				self.mot.ajouter_Lettre(self)
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True

			# Si la lettre en haut à gauche est cliqué
			# Si la lettre en haut à droite est cliqué
			# Si la lettre en bas ç gauche est cliqué
			# Si la lettre en bas à droite est cliqué
	"""