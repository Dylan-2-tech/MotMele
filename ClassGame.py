from tkinter import *
from tkinter import ttk
import tkinter.font as font
import random
import string
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
			liste_de_grille[i] = liste_de_grille[i].replace('grille/','') # For ubuntu
			liste_de_grille[i] = liste_de_grille[i].replace('grille\\','') # For windows
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

		# Boutton pour creer des grilles
		self.CreationBoutton = Button(self.CreationLabelFrame,text = "Creer",font = font.Font(size = 15), bg = "#3B706E", fg = "white",
		 activebackground = "#448784", activeforeground = "white", command = self.go_creation)
		self.CreationBoutton.pack(pady = 5)

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
		self.GameButton = Button(self,text = "JOUER",fg = "white", font = font.Font(size = 15),bg = "#6E64A2", activebackground = "#8177B4",activeforeground = "white", command = lambda:self.launch_game())
		self.GameButton.pack(pady = 50)

		# Boutton pour quitter la partie
		self.leaveBtn = Button(self,text="Quitter",bg = "#C22955", activebackground = "#D7436D",activeforeground = "white",
		 fg = "white",command = self.destroy, font = font.Font(size=15))
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

	def go_creation(self):
		self.destroy()
		Creation()


# Classe de la fenetre de création de grille
class Creation(Tk):

	def __init__(self):
		super().__init__()

		self.title("Création de grilles") # Titre du jeu
		self.geometry("1200x700+300+150") # Dimmension de la fenetre
		self.minsize(width = 1200, height = 700) # Dimmension minimum de la fenetre
		self.maxsize(width = 1200, height = 700) # Dimmension maximale de la fenetre
		self.configure(bg="#45458B") # Couleur de fond

		# Toutes les lettres de l'alphabet en majuscules
		self.letters = string.ascii_uppercase

		# Label Frame qui va contenir la grille et les options de création
		self.GrilleLabelFrame = LabelFrame(self, text = "Grille", labelanchor = 'n', bg = "#45458B", font = font.Font(size = 20))
		self.GrilleLabelFrame.pack(side = LEFT, fill = Y,pady = 20, padx = 20)

		# Double liste des entré qui vont prendre les lettre du joueur pour créer la grille
		self.entryGrille = [[Entry(self.GrilleLabelFrame,font = font.Font(size = 25), width = 2,bg = "#555591") for i in range(9)] for i in range(9)]
		# Double liste de charactère vide qui représente la grille que le joueur va créer
		self.nouvelleGrille = [["" for i in range(9)] for i in range(9)]
		# Liste des mots que le joueur veut ajouter
		self.listeMot = []

		# Frame qui va comporter l'entré pour le nom de la grille
		self.nomFrame = Frame(self.GrilleLabelFrame, bg = "#45458B")
		self.nomFrame.pack(side = TOP,padx = 75)
		self.pack_propagate(0)

		# Label qui précise où entrer le nom de la grille que le joueur veut générer
		self.nomLabel = Label(self.nomFrame, text = "Nom:", bg = "#45458B", fg = "white", font = font.Font(size = 15))
		self.nomLabel.pack(side = LEFT)

		# Entry qui va prendre le nom de la grille que le joueur veut créer
		self.fileName = Entry(self.nomFrame, font = font.Font(size = 15),bg = "#555591")
		self.fileName.pack(side = TOP)

		# label qui va contenir les options au fonds du labelFrame
		self.OptionLabel = Label(self.GrilleLabelFrame, bg = "#45458B")
		self.OptionLabel.pack(side = BOTTOM, fill = X,padx = 80, pady = 10)

		# Bouton pour deséléctionné toutes les lettres
		self.ClearLettersBtn = Button(self.OptionLabel,text = "Clear",bg = "#337292", activebackground = "#4991B6",
		 font = font.Font(size = 14), fg = "white", command = self.clear)
		self.ClearLettersBtn.pack(side = RIGHT)

		# Boutton pour creer des grilles
		self.CreationBoutton = Button(self.OptionLabel,text = "Générer",font = font.Font(size = 15), bg = "#2C8031",
		 fg = "white", activebackground = "#3E9D44", activeforeground = "white",command = self.transformer)
		self.CreationBoutton.pack(pady = 5, side = LEFT)

		# LabelFrame qui va contenir l'affichage de la grille généré par le joueur
		self.AffichageLabelFrame = LabelFrame(self, text = "Affichage", font = font.Font(size = 20), width = 425, labelanchor = 'n', bg = "#45458B")
		self.AffichageLabelFrame.pack(side = RIGHT, fill = Y, pady = 20, padx = 20)
		self.AffichageLabelFrame.pack_propagate(0)

		# Double liste de Label qui vont représenté la grille du joueur lors de l'affichage
		self.lettreLabelListe = [[Label(self.AffichageLabelFrame, bg = "#45458B", font = font.Font(size = 25), text = self.nouvelleGrille[x][y]) for y in range (9)] for x in range (9)]

		# Boutton pour revenir au menu
		self.leaveBtn = Button(self,text="Revenir au Menu",bg = "#C22955", activebackground = "#D7436D", fg = "white",
			activeforeground = "white",command = self.back_menu, font = font.Font(size=15))
		self.leaveBtn.pack()

		# Frame bidon qui sert à 'centrer' la listbox
		self.bidonFrame = Frame(self,bg = "#45458B", height = 200)
		self.bidonFrame.pack(side = BOTTOM)

		# LabelFrame qui va comprendre la liste box des mots à trouver dans la grille
		self.MotATrouveLabelFrame = LabelFrame(self, text = "Liste de mots", font = font.Font(size = 15), bg = "#45458B")
		self.MotATrouveLabelFrame.pack(fill = X, side = BOTTOM, pady = 20, ipadx = 20)

		# Frame qui va comporter l'entrée du mot et le boutton supprimer
		self.MotOptionFrame = Frame(self.MotATrouveLabelFrame, bg = "#45458B")#45458B
		self.MotOptionFrame.pack(fill = X, side = TOP)

		# Entrée qui va accueillir le mot que le joueur veut ajouter à sa liste
		self.MotEntry = Entry(self.MotOptionFrame, bg = "#555591", font = font.Font(size = 15))
		self.MotEntry.pack(side = TOP)
		self.MotEntry.bind('<Return>',lambda event:self.add_mot())

		# Boutton pour retirer le mot sélectionné
		self.suppMot = Button(self.MotOptionFrame, text = "Supprimer", bg = "#C22955", activebackground ="#D7436D",
			font = font.Font(size = 12), command = self.supprimer_mot)
		self.suppMot.pack(side = TOP, pady = 10)

		# List Box qui va comporter la liste de mots que le joueur doit trouver
		self.var = StringVar(value = self.listeMot)
		self.ListeBoxMotATrouver = Listbox(self.MotATrouveLabelFrame, font = font.Font(size = 17), width = 16 ,
			activestyle = 'none', selectbackground = "#505092", bg = "#45458B", fg = "black",
			borderwidth=0, highlightthickness=0, listvariable = self.var)
		self.ListeBoxMotATrouver.pack(fill = BOTH)

		# Boutton pour enregistrer la grille généré en fichier txt ainsi que les mot
		self.SaveButton = Button(self.AffichageLabelFrame,text = "Enregistrer", bg = "#644D8B", activebackground = "#755CA0",
			font = font.Font(size = 30), command = self.save_grille)
		self.SaveButton.pack(side = BOTTOM, pady = 75) 

		# Affichage des labels pour l'affichage des lettres de la grille
		posy = 20
		for listeLabel in self.lettreLabelListe:
			posx = 15
			for label in listeLabel:
				label.place(x = posx, y = posy)
				posx += 45
			posy += 45

		# Affichage de la grille d'entrée
		posy = 50
		for listeEntry in self.entryGrille:
			posx = 10
			for entry in listeEntry:
				entry.place(x = posx, y = posy)
				posx += 45
			posy += 45

		self.mainloop()

	def back_menu(self):
		self.destroy()
		Menu()


	def save_grille(self):
		# vérification si un fichier existe déjà en ce nom
		liste_de_grille = glob.glob("grille/*.txt")
		liste_de_mot = glob.glob("mot/*.txt")
		fileName = self.fileName.get()

		for i in range(len(liste_de_grille)):
			liste_de_grille[i] = liste_de_grille[i].replace('grille/','') # For ubuntu
			liste_de_grille[i] = liste_de_grille[i].replace('grille\\','') # For windows
			liste_de_grille[i] = liste_de_grille[i].replace('.txt','')

		print(liste_de_mot)

		for i in range(len(liste_de_mot)):
			if len(liste_de_mot) > 0:
				liste_de_mot[i] = liste_de_mot[i].replace('grille/','') # For ubuntu
				liste_de_mot[i] = liste_de_mot[i].replace('grille\\','') # For windows
				liste_de_mot[i] = liste_de_mot[i].replace('.txt','')

		if fileName not in liste_de_mot and fileName not in liste_de_grille:
			with open(f"grille/{fileName}.txt", 'w') as grilleFile:
				for x in range(9):
					for y in range(9):
						if y == 8:
							grilleFile.write(self.nouvelleGrille[x][y])
						else:
							grilleFile.write(self.nouvelleGrille[x][y]+',')
					grilleFile.writelines("\n")
			print("Grille créé correctement")

			with open(f"mot/{fileName}.txt", 'w') as motFile:
				for i in range(len(self.listeMot)):
					if i == len(self.listeMot)-1:
						motFile.write(self.listeMot[i])
					else:
						motFile.write(self.listeMot[i]+',')
			print("Mot créé correctement")




	def supprimer_mot(self):
		try:
			self.listeMot.pop(self.ListeBoxMotATrouver.curselection()[0])
			self.var.set(self.listeMot)
		except:
			self.ERRORLABEL = Label(self, bg = "#45458B", fg = "red", font = font.Font(size = 14),
				text = "Veuillez sélectionner un mot")
			self.ERRORLABEL.pack(side = BOTTOM, pady = 10)					
			self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)


	def add_mot(self):
		if len(self.listeMot) < 10:
			if not self.space_word() and not self.MotEntry.get() == "":
				self.listeMot.append(self.MotEntry.get())
				self.MotEntry.delete(0,len(self.MotEntry.get()))
				self.var.set(self.listeMot)
			else:
				self.ERRORLABEL = Label(self, bg = "#45458B", fg = "red", font = font.Font(size = 14),
					text = "Entrez un mot sans espaces")
				self.ERRORLABEL.pack(side = BOTTOM, pady = 10)
				self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)

		else:
			self.ERRORLABEL = Label(self, bg = "#45458B", fg = "red", font = font.Font(size = 14),
				text = "Nombre maximum de 10 mots")
			self.ERRORLABEL.pack(side = BOTTOM, pady = 10)
			self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)


	def space_filename(self):
		fileName = self.fileName.get()
		indc = 0
		space = False

		while not space and indc < len(fileName):
			space = fileName[indc] == " "
			indc += 1

		return space

	def space_word(self):
		word = self.MotEntry.get()
		indc = 0
		space = False

		while not space and indc < len(word):
			space = word[indc] == " "
			indc += 1

		return space


	# Méthode qui s'occupe de l'affichage de la grille généré par le joueur
	def affichage_grille(self):
		for x in range(9):
			for y in range(9):
				self.lettreLabelListe[y][x].configure(text = self.nouvelleGrille[y][x])
		

	# Méthode pour nettoyer les les mots inseré par le joueur
	def clear(self):
		for listeEntry in self.entryGrille:
			for entry in listeEntry:
				entry.delete(0,len(entry.get()))


	# Méthode qui retourne vrai si le joueur a entré plus d'une lettre dans l'entrée
	def plus_une_lettre(self):
		for x in range(len(self.entryGrille)):
				for y in range(len(self.entryGrille[0])):
					if len(self.entryGrille[x][y].get()) > 1:
						return True
		return False


	# Méthode qui transforme la nouvelle grille en vrai grille à l'aide des entrée
	def transformer(self):
		if len(self.fileName.get()) > 3:
			if not self.space_filename():
				if self.plus_une_lettre():
					self.ERRORLABEL = Label(self.GrilleLabelFrame, bg = "#45458B", fg = "red", font = font.Font(size = 14),
						text = "Insérez qu'une seule lettre dans chaque case")
					self.ERRORLABEL.pack(side = BOTTOM, pady = 10)					
					self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)
				else:
					for x in range(len(self.entryGrille)):
						for y in range(len(self.entryGrille[0])):
							if self.entryGrille[x][y].get() != "":
								self.nouvelleGrille[x][y] = self.entryGrille[x][y].get().upper()
							else:
								self.nouvelleGrille[x][y] = self.letters[random.randint(0,25)]
					self.ERRORLABEL = Label(self.GrilleLabelFrame, bg = "#45458B", fg = "green", font = font.Font(size = 14),
						text = f"La grille {self.fileName.get()} est généré")
					self.ERRORLABEL.pack(side = BOTTOM, pady = 10)					
					self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)

					self.affichage_grille()
			else:
				self.ERRORLABEL = Label(self.GrilleLabelFrame, bg = "#45458B", fg = "red", font = font.Font(size = 14),
					text = "Pas d'espaces dans le nom")
				self.ERRORLABEL.pack(side = BOTTOM, pady = 10)					
				self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)

		else:
			self.ERRORLABEL = Label(self.GrilleLabelFrame, bg = "#45458B", fg = "red", font = font.Font(size = 14),
				text = "Minimum 4 lettres dans le nom de la grille")
			self.ERRORLABEL.pack(side = BOTTOM, pady = 10)					
			self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)




# Class de la fenetre de jeu
class Jeu(Tk):

	def __init__(self,grille):
		super().__init__()

		# Grille du jeu

		self.grille = [line.split(',') for line  in open(f"grille/{grille}.txt")]

		for listLettre in self.grille:
			for i in range(len(listLettre)):
				listLettre[i] = listLettre[i].replace('\n','')

		# Liste des mots à trouver
		self.listeMot = [mot.upper().split(',') for mot in open(f"mot/{grille}.txt")][0]
		self.listeMotTrouve = [] # Liste des mot déjà trouvé

		# Initialisation de la fenetre du jeu
		self.title("Mot Mélé") # Titre du jeu
		self.geometry("1200x735+270+150") # Dimmension de la fenetre
		self.minsize(width = 1200, height = 735) # Dimmension minimum de la fenetre
		self.maxsize(width = 1200, height = 735) # Dimmension maximale de la fenetre
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
		self.valideBtn = Button(self.GameFrame, text = "Valider", bg = "#2C8031", activebackground = "#3E9D44", fg = "white", 
			activeforeground = "white", height = 1, font = font.Font(size = 14), command = self.valider)
		self.valideBtn.place(x = 150, y = 170)

		# Bouton pour deséléctionné toutes les lettres
		self.ClearLettersBtn = Button(self.GameFrame,text = "Clear",bg = "#337292", activebackground = "#4991B6",fg = "white",
			activeforeground = "white", font = font.Font(size = 14) , command = self.clear)
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

		# Boutton pour revenir au menu
		self.leaveBtn = Button(self.GameFrame,text="Revenir au Menu",bg = "#C22955", activebackground = "#D7436D", fg = "white",
			activeforeground = "white",command = self.back_menu, font = font.Font(size=15))
		self.leaveBtn.place(x = 325, y = 550) # emplacement forcé sur des pixel précis

		# Mot qui va changer au fur et à mesure de la partie
		self.mot = Mot()

		# génération de la map des lettres
		posy = 40 # position y du boutton de la lettre
		for x in range(len(self.grille)): # on parcours la map en x
			posx = 40 # La position initiale de chaque boutton en x est donc 0 pour la premiere ligne
			for y in range(len(self.grille[0])): # On parcours la map en y
				lettre = Lettre(self.grille[x][y].upper(),x,y,self) # on initialise les lettre grâce à la classe Lettre
				lettre.boutton.place(x=posx, y=posy) # on place le boutton de la lettre qui correspond à la position grille[x][y]
				self.grille[x][y] = lettre
				posx+=75 # On incrémente de 100 la position en x pour laisser quelques pixels pour d'écart en horizontal
			posy += 75 # On incrémente de 115 la position en y pour laisser un espace de quelques pixels d'écart en vertical

		self.mainloop() # Affichage de la fenetre


	# Méthode qui nettoie les lettres sélectionner mais pas validé
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
					self.ERRORLABEL = Label(self.GameFrame, bg = "#45458B", fg = "green", font = font.Font(size = 20),
						text = "Tu as gagné !")
					self.ERRORLABEL.pack(side = TOP)					
					self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)
					# arreter le timer
				else:
					self.ERRORLABEL = Label(self.GameFrame, bg = "#45458B", fg = "green", font = font.Font(size = 20),
						text = "Vous avez trouvé le mot !")
					self.ERRORLABEL.pack(side = TOP)					
					self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)
				
			elif mot in self.listeMotTrouve: # Si le mot est déjà trouvé
				self.ERRORLABEL = Label(self.GameFrame, bg = "#45458B", fg = "red", font = font.Font(size = 20),
					text = "Mot déjà trouvé")
				self.ERRORLABEL.pack(side = TOP)					
				self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)

			else: # Si le mot n'est pas le bon
				self.ERRORLABEL = Label(self.GameFrame, bg = "#45458B", fg = "red", font = font.Font(size = 20),
					text = "Pas le bon mot :/")
				self.ERRORLABEL.pack(side = TOP)					
				self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)

		else: # Si le mot n'est pas correct
			self.ERRORLABEL = Label(self.GameFrame, bg = "#45458B", fg = "red", font = font.Font(size = 20),
				text = "Le mot n'est pas valide")
			self.ERRORLABEL.pack(side = TOP)					
			self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)

		self.mot.clear_mot()
		self.clear()

		
	def back_menu(self):
		self.destroy()
		Menu()


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
