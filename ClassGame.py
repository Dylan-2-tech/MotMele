from tkinter import *
from tkinter import ttk
import tkinter.font as font


#### Fichier des class du jeu ####

# Class menu pour la personnalisation du jeu et lancement du jeu
class Menu(Tk):

	def __init__(self):
		super().__init__()
		self.title("Menu") # Titre du jeu
		self.geometry("500x200+400+250") # Dimmension de la fenetre
		self.minsize(width = 500, height = 200) # Dimmension minimum de la fenetre
		self.maxsize(width = 500, height = 200) # Dimmension maximale de la fenetre
		self.configure(bg="#45458B")

		self.GameButton = Button(self,text = "jouer", command = lambda:launch_game(self))
		self.GameButton.pack()

		# Boutton pour quitter la partie
		self.leaveBtn = Button(self,text="Quitter",bg = "red", activebackground = "red", fg = "white",command = self.destroy, font = font.Font(size=15))
		self.leaveBtn.pack()

		def launch_game(self):
			self.destroy()
			Jeu()

		self.mainloop()



# Class de la fenetre de jeu
class Jeu(Tk):

	def __init__(self):
		super().__init__()

		# Map du jeu
		self.gameMap = [ 
					["P","O","U","R","I","Z","Y","I"],
					["B","H","S","E","W","Q","U","A"],
					["H","R","I","V","P","O","V","W"],
					["L","J","R","E","I","M","R","F"],
					["E","X","I","N","K","W","T","Y"],
					["X","O","T","L","G","Y","H","O"],
					["V","J","A","R","O","Y","F","P"],
					["P","M","H","E","I","M","A","U"]
					]

		self.listeMot = ["POUR","IRIS","REVE"] # Liste de mot à trouvé dans la map
		self.listeMotTrouve = [] # Liste des mot déjà trouvé

		# Initialisation de la fenetre du jeu
		self.title("Mot Mélé") # Titre du jeu
		self.geometry("1200x650+400+250") # Dimmension de la fenetre
		self.minsize(width = 1200, height = 650) # Dimmension minimum de la fenetre
		self.maxsize(width = 1200, height = 650) # Dimmension maximale de la fenetre
		self.configure(bg="#45458B")

		# Actuel taille en largeur de la fenetre du jeu self.winfo_width()
		# Actuel taille en hauteur de la fenetre du jeu self.winfo_height()


		# Frame qui va comporter tout les boutons pour valider etc
		self.GameFrame = Frame(self, width = 500,height = 600, bg = "#45458B")
		self.GameFrame.pack(side = RIGHT)
		self.GameFrame.pack_propagate(0)

		# Label Frame qui va prendre en son centre l'affichage du mot
		self.MotLabelFrame = LabelFrame(self.GameFrame,text = "Mot", width = 250, bg = "#45458B", font = font.Font(size = 17), labelanchor = 'n')
		self.MotLabelFrame.pack(ipadx = 20, ipady = 5, pady = 20)

		# Label qui affiche le mot séléctionné
		self.MotLabel = Label(self.MotLabelFrame,bg = "#45458B", font = font.Font(size=20),fg = "white")
		self.MotLabel.pack()#place(x = 900, y = 200)

		# Boutton pour valider la sélection des lettres
		self.valideBtn = Button(self.GameFrame, text = "Valider", bg = "green", activebackground = "green", fg = "white", height = 1, font = font.Font(size = 14), command = lambda:valider(self))
		self.valideBtn.place(x = 150, y = 170)

		# Bouton pour deséléctionné toutes les lettres
		self.ClearLettersBtn = Button(self.GameFrame,text = "Clear",bg = "light blue", activebackground = "light blue", font = font.Font(size = 14) , command = lambda:clear(self))
		self.ClearLettersBtn.place(x = 300, y = 170)

		# Label Frame qui va prendre en son intérieur les mots à trouver
		self.MotATrouveLabelFrame = LabelFrame(self.GameFrame, text = "Mots à trouvé", font = font.Font(size = 17), bg = "#45458B")
		self.MotATrouveLabelFrame.place(x = 150, y = 250)#pack(ipadx = 20, ipady = 10, pady = 150)

		# ListBox qui va afficher les mots à trouvé
		self.var = StringVar(value = self.listeMot)
		self.ListeBoxMotATrouver = Listbox(self.MotATrouveLabelFrame, font = font.Font(size = 14), width = 16 ,
			activestyle = 'none', selectbackground = "#45458B", bg = "#45458B",
			borderwidth=0, highlightthickness=0, listvariable = self.var)
		self.ListeBoxMotATrouver.pack(pady = 10, padx = 10)

		# Boutton pour quitter la partie
		self.leaveBtn = Button(self.GameFrame,text="Revenir au Menu",bg = "red", activebackground = "red", fg = "white",command= lambda:back_menu(self), font = font.Font(size=15))
		self.leaveBtn.place(x = 325, y = 550) # emplacement forcé sur des pixel précis

		# Label qui affiche si le mot séléctionné est bon ou pas
		self.ValideLabel = Label(self.GameFrame,bg = "#45458B", font = font.Font(size=20))
		self.ValideLabel.pack(side = TOP)#place(x = 750, y = 250)


		# Mot qui va changer au fur et à mesure de la partie
		self.mot = Mot()

		# Fonction qui nettoie les lettres sélectionner mais pas validé
		def clear(self):
			self.mot.clear_mot()
			self.MotLabel.configure(text = self.mot.get_mot())
			for listeLettre in self.gameMap:
				for lettre in listeLettre:
					if lettre.isClicked and not lettre.isValid:
						lettre.isClicked = False
						lettre.boutton.configure(bg = "#9090EE",activebackground="#A3A3FE")

		# Méthode Valider
		def valider(self):

			if self.mot.mot_correct(): # Si le mot est correct
				indMot = 0
				trouve = False
				mot = self.mot.get_mot()

				while not trouve and indMot < len(self.listeMot): # On recherche le mot pour savoir si le joueur à trouvé le bon
					trouve = self.listeMot[indMot] == mot # True si le mot est dans la liste
					indMot += 1

				if trouve: # Si on la trouvé
					self.listeMotTrouve.append(mot)
					self.listeMot.pop(indMot-1)
					self.var.set(self.listeMot)
					self.mot.valider_mot()
					if len(self.listeMot) == 0:
						self.ValideLabel.configure(text = "Tu as gagné", fg = "green")
						# arreter le timer
					else:
						self.ValideLabel.configure(text = "Vous avez trouvé le mot !", fg = "green")
					
				elif mot in self.listeMotTrouve: # Si le mot est déjà trouvé
					self.ValideLabel.configure(text = "Mot déjà trouvé", fg = "red")
				else: # Si le mot n'est pas le bon
					self.ValideLabel.configure(text = "Pas le bon mot :/", fg = "red")

			else: # Si le mot n'est pas correct
				self.ValideLabel.configure(text = "Le mot n'est pas valide", fg = "red")

			self.mot.clear_mot()
			clear(self)
		
		def back_menu(self):
			self.destroy()
			Menu()



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


# Class des lettres
class Lettre:

	def __init__(self,lettre,x,y,game):

		self.game = game
		self.MotLabel = game.MotLabel
		self.mot = game.mot
		self.isValid = False # Si le mot est validé
		self.isClicked = False # Si il est cliqué alors
		self.x = x # position x de la lettre
		self.y = y # position y de la lettre
		self.lettre = lettre
		self.boutton = Button(game,text="".join(lettre),
			width = 3, height = 1, font = font.Font(size=20),
			bg="#9090EE", activebackground="#A3A3FE", bd=0,
			command=self.clicked)
	
	def clicked(self): # méthode qui s'active quand la lettre est cliqué

		if self.isClicked and not self.isValid: # Si la lettre est déja cliqué
			self.boutton.configure(bg = "#9090EE",activebackground="#A3A3FE") # On remet une couleur par défaut 
			self.isClicked = False # Elle devient plus cliqué
			self.mot.text = [self.mot.text[i] for i in range(len(self.mot.text)) if self != self.mot.text[i]] # On retire la lettre du mot
			self.MotLabel.configure(text = self.mot) # Affichage du mot en cours
		
		elif not self.isClicked and not self.isValid: # Si la lettre n'est pas encore cliqué et quelle est pas validé
			self.boutton.configure(bg = "#995AD1",activebackground="#995AD1") # On change sa couleur pour dire qu'elle est cliqué
			self.isClicked = True # Elle devient cliqué
			self.mot.ajouter_Lettre(self) # On l'ajoute au mot
			self.MotLabel.configure(text = self.mot) # Affichage du mot en cours

		elif self.isClicked and self.isValid: # Si la lettre est déjà cliqué et déjà validé
			self.mot.ajouter_Lettre(self) # On l'ajoute au mot
			self.MotLabel.configure(text = self.mot) # Affichage du mot en cours



# Class du mot
class Mot:

	def __init__(self):
		self.text = []

	def __str__(self):
		return "".join(self.text[i].lettre for i in range(len(self.text)))

	def get_mot(self):
		return "".join(self.text[i].lettre for i in range(len(self.text)))

	def clear_mot(self):
		self.text = []

	def valider_mot(self):
		for lettre in self.text:
			lettre.isValid = True
			lettre.boutton.configure(bg = "green", activebackground = "#359221")

	def ajouter_Lettre(self, lettre):
		self.text.append(lettre)

	def mot_correct(self):
		"""Renvoie True si chaque lettre du mot suivent la même direction.

		En mathématiques, (x,y) sont les coordonnées basiques d'un graphe pour trouver un point.
		En informatique lorsqu'on veux créer une map en 2D n ne peut pas utiliser cette représentation
		des positions des objet que l'on veut placer dans la map.
		Une "MAP" en info c'est une liste de liste.
		Supposons que nous avons une map comme la suivante:

			Map = [["a","b","c","d"],
				   ["e","f","g","h"],
				   ["i","j","k","l"]]

		En graphe le point à la position (3,4) est "l" mais en informatique c'est Map[3][2].
		On soustrain 1 au deux coordonnées et on place d'abord les y puis les x.
		"""

		if len(self.text) > 1: # Si le mot a plus de une seule lettre
			if self.mot_horizontal(): # Si le mot est horizontal
				return True
			elif self.mot_vertical(): # Si le mot est vertical
				return True
			elif self.mot_diagonale_gauche_droite(): # Si le mot est en diagonale de gauche à droite
				return True
			elif self.mot_diagonale_droite_gauche(): # Si le mot est en diagonale de droite à gauche
				return True
			else: # Si le mot n'est pas bien formé
				return False
		else: # Si le mot est composé de qu'une seule lettre
			return False
	

	def mot_horizontal(self):
		# Si toutes les lettres sont positionné horizontalement

		startX = self.text[0].x # Position x pour comparer les positions avec self.text[indLetter].x
		startY = self.text[0].y # Position y pour comparer les positions avec self.text[indLetter].y
		indLetter = 1 # Indice pour comparer les position entre lettres. On commence avec la 2ème lettre car startX et startY sont les position de la première lettre
		wellFormed = True # Booléen pour entrer dans la boucle 

		while wellFormed and indLetter < len(self.text): # Tant que le mot semble être horizontale et qu'on a pas fini de le parcourir
			# ENORME condition pour savoir si les lettres se suivent horizontalement
			wellFormed = (self.text[indLetter].x == startX and self.text[indLetter].y == startY+1) or (self.text[indLetter].x == startX and self.text[indLetter].y == startY-1)
			startY = self.text[indLetter].y # On actualise la position en y avec celle de la lettre comparé au tour d'avant 
			indLetter += 1 # On augmente pour comparer avec la lettre suivante

		if wellFormed: # Si le mot est bien formé
			return True # On retourne True
		else: # Sinon
			return False # On retourne False

	def mot_vertical(self):
		# Si toutes les lettres sont positionné verticalement

		startX = self.text[0].x # Position x pour comparer les positions avec self.text[indLetter].x
		startY = self.text[0].y # Position y pour comparer les positions avec self.text[indLetter].y
		indLetter = 1 # Indice pour comparer les position entre lettres. On commence avec la 2ème lettre car startX et startY sont les position de la première lettre
		wellFormed = True # Booléen pour entrer dans la boucle 

		while wellFormed and indLetter < len(self.text): # Tant que le mot semble être verical et qu'on a pas fini de le parcourir
			# ENORME condition pour savoir si les lettres se suivent verticalement
			wellFormed = (self.text[indLetter].x == startX+1 and self.text[indLetter].y == startY) or (self.text[indLetter].x == startX-1 and self.text[indLetter].y == startY)
			startX = self.text[indLetter].x # On actualise la position en x avec celle de la lettre comparé au tour d'avant 
			indLetter += 1 # On augmente pour comparer avec la lettre suivante

		if wellFormed: # Si le mot est bien formé
			return True # On retourne True
		else: # Sinon
			return False # On retourne False

	def mot_diagonale_gauche_droite(self):
		# Si toutes les lettres sont positionnées en diagonale de à gauche à droite

		startX = self.text[0].x # Position x pour comparer les positions avec self.text[indLetter].x
		startY = self.text[0].y # Position y pour comparer les positions avec self.text[indLetter].y
		indLetter = 1 # Indice pour comparer les position entre lettres. On commence avec la 2ème lettre car startX et startY sont les position de la première lettre
		wellFormed = True # Booléen pour entrer dans la boucle 

		while wellFormed and indLetter < len(self.text):
			# ENORME condition pour savoir si les lettres se suivent en diagonale de à gauche à droite
			wellFormed = (self.text[indLetter].x == startX+1 and self.text[indLetter].y == startY+1) or (self.text[indLetter].x == startX-1 and self.text[indLetter].y == startY-1)
			startX = self.text[indLetter].x # On actualise la position en x avec celle de la lettre comparé au tour d'avant
			startY = self.text[indLetter].y # On actualise la position en y avec celle de la lettre comparé au tour d'avant
			indLetter += 1 # On augmente pour comparer avec la lettre suivante

		if wellFormed: # Si le mot est bien formé
			return True # On retourne True
		else: # Sinon
			return False # On retourne False

	def mot_diagonale_droite_gauche(self):
		# Si toutes les lettres sont positionnées en diagonale de droite à gauche

		startX = self.text[0].x # Position x pour comparer les positions avec self.text[indLetter].x
		startY = self.text[0].y # Position y pour comparer les positions avec self.text[indLetter].y
		indLetter = 1 # Indice pour comparer les position entre lettres. On commence avec la 2ème lettre car startX et startY sont les position de la première lettre
		wellFormed = True # Booléen pour entrer dans la boucle 

		while wellFormed and indLetter < len(self.text):
			# ENORME condition pour savoir si les lettres se suivent en diagonale de droite à gauche
			wellFormed = (self.text[indLetter].x == startX+1 and self.text[indLetter].y == startY-1) or (self.text[indLetter].x == startX-1 and self.text[indLetter].y == startY+1)
			startX = self.text[indLetter].x # On actualise la position en x avec celle de la lettre comparé au tour d'avant
			startY = self.text[indLetter].y # On actualise la position en y avec celle de la lettre comparé au tour d'avant
			indLetter += 1 # On augmente pour comparer avec la lettre suivante

		if wellFormed: # Si le mot est bien formé
			return True # On retourne True
		else: # Sinon
			return False # On retourne False
