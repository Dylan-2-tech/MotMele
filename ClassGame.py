from tkinter import *
from tkinter import ttk
import tkinter.font as font
import glob


#### Fichier des class du jeu ####

# Class menu pour la personnalisation du jeu et lancement du jeu
class Menu(Tk):

	def __init__(self):
		super().__init__()
		self.title("Menu") # Titre du jeu
		self.geometry("1000x500+400+250") # Dimmension de la fenetre
		self.minsize(width = 1000, height = 500) # Dimmension minimum de la fenetre
		self.maxsize(width = 1000, height = 500) # Dimmension maximale de la fenetre
		self.configure(bg="#45458B") # Couleur de fond

		liste_de_grille = glob.glob("grille/*.txt")

		for i in range(len(liste_de_grille)):
			liste_de_grille[i] = liste_de_grille[i].replace('grille/','')
			liste_de_grille[i] = liste_de_grille[i].replace('.txt','')

		# Frame qui va occuper tout le haut du menu et qui va comporter la phrase de Menu
		self.MenuFrame = Frame(self, bg = "red", height = 100)
		self.MenuFrame.pack(fill = X, side = TOP)
		self.MenuFrame.pack_propagate(0)

		# Label du menu
		self.MenuLabel = Label(self.MenuFrame, bg = "#45458B" , fg = "black", text = "Menu du jeu", font = font.Font(size = 30))
		self.MenuLabel.pack(fill = BOTH, expand = True)

		# Label Frame de la personnalisation des couleurs du jeu
		self.PersonnalisationLabelFrame = LabelFrame(self, text = "Personnalisation", bg = "#45458B", width= 300, font = font.Font(size = 20), labelanchor = 'n')
		self.PersonnalisationLabelFrame.pack(side = LEFT, ipady = 10, ipadx = 20, pady = 20, padx = 20, fill = Y)

		# Label Frame de la création de grille de jeu
		self.CreationLabelFrame = LabelFrame(self, text = "Création de Grilles", bg = "#45458B", width= 300, font = font.Font(size = 20), labelanchor = 'n')
		self.CreationLabelFrame.pack(side = RIGHT, ipady = 10, ipadx = 20, pady = 20, padx = 20, fill = Y)

		# Label Frame pour charger une grille de jeu
		self.ChargerGrilleLabelFrame = LabelFrame(self.CreationLabelFrame, text = "Charger", bg = "#45458B", font = font.Font(size = 15))
		self.ChargerGrilleLabelFrame.pack(side = BOTTOM, ipady = 5, ipadx = 5, pady = 10, padx= 10, fill = BOTH)

		self.var = StringVar(value = liste_de_grille) # Liste des grilles 
		# List box qui va comporter les grilles que le joueur peut Charger
		self.GrilleListBox = Listbox(self.ChargerGrilleLabelFrame, bg = "#6D5EBD",
			activestyle = 'none', selectbackground = "#6D5EBD", font = font.Font(size = 15),
			borderwidth=0, highlightthickness=0, listvariable = self.var)
		self.GrilleListBox.pack(fill = BOTH, expand = True)

		# Boutton qui permet de fermer la fenetre du menu et de lancer le jeu
		self.GameButton = Button(self,text = "JOUER",fg = "white", font = font.Font(size = 15),bg = "#6E64A2", activebackground = "#8177B4",activeforeground = "white", command = lambda:launch_game(self))
		self.GameButton.pack(pady = 50)

		# Boutton pour quitter la partie
		self.leaveBtn = Button(self,text="Quitter",bg = "#C22955", activebackground = "#D7436D",activeforeground = "white", fg = "white",command = self.destroy, font = font.Font(size=15))
		self.leaveBtn.pack(side = BOTTOM, pady = 30)


		# Méthode qui va servir de lancer la partie et de fermer la fnetre du menu
		def launch_game(self):
			# Etape de préparation pour voir si la grille séléctionné à des mots ou non
			try:
				grille = self.GrilleListBox.get(self.GrilleListBox.curselection())

				if glob.glob(f"mot/{grille}.txt") == []: # Si la grille n'a pas de mot
					# Affichage du label de l'erreur
					self.ERRORLABEL = Label(self, text = "La grille n'a pas de mots attitrés", bg = "#45458B", fg = "red", font = font.Font(size = 15))
					self.ERRORLABEL.pack()
					self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)
				else:
					self.destroy()
					Jeu(grille)
			except:
				self.ERRORLABEL = Label(self, text = "Veuillez choisir une grille", bg = "#45458B", fg = "red", font = font.Font(size = 15))
				self.ERRORLABEL.pack()
				self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)

		self.mainloop()


# Class de la fenetre de jeu
class Jeu(Tk):

	def __init__(self,grille):
		super().__init__()

		# Map du jeu

		self.grille = [line.split(',') for line  in open(f"grille/{grille}.txt")]

		for listLettre in self.grille:
			for i in range(len(listLettre)):
				listLettre[i] = listLettre[i].replace('\n','')

		self.listeMot = [mot.split(',') for mot in open(f"mot/{grille}.txt")][0]# # Liste de mot à trouvé dans la map
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
		self.valideBtn = Button(self.GameFrame, text = "Valider", bg = "#2C8031", activebackground = "#3E9D44", fg = "white",activeforeground = "white", height = 1, font = font.Font(size = 14), command = lambda:valider(self))
		self.valideBtn.place(x = 150, y = 170)

		# Bouton pour deséléctionné toutes les lettres
		self.ClearLettersBtn = Button(self.GameFrame,text = "Clear",bg = "#337292", activebackground = "#4991B6",fg = "white",activeforeground = "white", font = font.Font(size = 14) , command = lambda:clear(self))
		self.ClearLettersBtn.place(x = 300, y = 170)

		# Label Frame qui va prendre en son intérieur les mots à trouver
		self.MotATrouveLabelFrame = LabelFrame(self.GameFrame, text = "Mots à trouvé", font = font.Font(size = 17), bg = "#45458B")
		self.MotATrouveLabelFrame.place(x = 150, y = 250)#pack(ipadx = 20, ipady = 10, pady = 150)

		# ListBox qui va afficher les mots à trouvé
		self.var = StringVar(value = self.listeMot)
		self.ListeBoxMotATrouver = Listbox(self.MotATrouveLabelFrame, font = font.Font(size = 14), width = 16 ,
			activestyle = 'none', selectbackground = "#45458B", bg = "#45458B",
			borderwidth=0, highlightthickness=0, listvariable = self.var)
		self.ListeBoxMotATrouver.pack()

		# Boutton pour quitter la partie
		self.leaveBtn = Button(self.GameFrame,text="Revenir au Menu",bg = "red", activebackground = "red", fg = "white",activeforeground = "white",command= lambda:back_menu(self), font = font.Font(size=15))
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
			for listeLettre in self.grille:
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
		for x in range(len(self.grille)): # on parcours la map en x
			posx = 40 # La position initiale de chaque boutton en x est donc 0 pour la premiere ligne
			for y in range(len(self.grille[0])): # On parcours la map en y
				lettre = Lettre(self.grille[x][y],x,y,self) # on initialise les lettre grâce à la classe Lettre
				lettre.boutton.place(x=posx, y=posy) # on place le boutton de la lettre qui correspond à la position grille[x][y]
				self.grille[x][y] = lettre
				posx+=75 # On incrémente de 100 la position en x pour laisser quelques pixels pour d'écart en horizontal
			posy += 75 # On incrémente de 115 la position en y pour laisser un espace de quelques pixels d'écart en vertical

		self.mainloop() # Affichage de la fenetre


# Class des lettres
class Lettre:

	def __init__(self,lettre,x,y,game):

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
