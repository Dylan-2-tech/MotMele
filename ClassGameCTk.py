import customtkinter
from customtkinter import CTk
from customtkinter import CTkButton
from customtkinter import CTkFont
from customtkinter import CTkFrame
from customtkinter import CTkLabel
from customtkinter import CTkEntry
from tkinter import CENTER
from tkinter import Listbox
from tkinter import StringVar
from tkinter import font
import random
import string
import glob

customtkinter.set_appearance_mode("dark")

#### Fichier des class du jeu ####

# Class menu pour la personnalisation du jeu et lancement du jeu
class Menu(CTk):

	def __init__(self):
		super().__init__()
		self.title("Menu") # Titre du jeu
		self.geometry("400x300+2000+250") # Dimmension de la fenetre
		self.minsize(width = 350, height = 250)
		self.maxsize(width = 450, height = 350)

		# Présentation des grilles du jeu dans la comboBox
		liste_de_grille = glob.glob("grille/*.txt")
		self.grille = ""

		for i in range(len(liste_de_grille)):
			liste_de_grille[i] = liste_de_grille[i].replace('grille/','') # Ubuntu
			liste_de_grille[i] = liste_de_grille[i].replace('grille\\','') # Windows
			liste_de_grille[i] = liste_de_grille[i].replace('.txt','')

		# Frame qui va occuper tout le haut du menu et qui va comporter la phrase de Menu
		self.MenuFrame = CTkFrame(self,height = 75)
		self.MenuFrame.grid(row = 0, column = 0, columnspan = 2, sticky = "WE", pady = (10,0), padx = 10)
		# Label du menu
		self.MenuLabel = CTkLabel(self.MenuFrame, text = "Mot Mélé", font = CTkFont(size = 30))
		self.MenuLabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)

		# Boutton qui permet de fermer la fenetre du menu et de lancer le jeu
		self.GameButton = CTkButton(self,text = "JOUER", font = CTkFont(size = 25), 
			fg_color = ("#8177B4","#6E64A2"), hover_color = ("#6E64A2","#8177B4"), command = self.launch_game)
		self.GameButton.grid(row = 1,column = 0)

		comboboxVar = customtkinter.StringVar(value = "Choisissez")
		# List box qui va comporter les grilles que le joueur peut Charger
		self.GrilleComboBox = customtkinter.CTkComboBox(self, font = CTkFont(size = 18),
			variable = comboboxVar, command = self.select_grille, values = liste_de_grille)
		self.GrilleComboBox.grid(row = 1, column = 1)

		# Boutton pour accéder à la page de création de Grilles
		self.CreationBoutton = CTkButton(self,text = "Creer",font = CTkFont(size = 20), command = self.go_creation,
			fg_color = ("#448784","#3B706E"), hover_color = ("#3B706E","#448784")) #self.go_creation
		self.CreationBoutton.grid(pady = (0,50), row = 2, columnspan = 2)
	
		# Configuration de l'adaptation de la page principale
		self.rowconfigure(1,weight = 1)
		self.columnconfigure(0, weight = 1)
		self.columnconfigure(1, weight = 1)


	def select_grille(self,choice):
		self.grille = choice

	# Méthode qui va servir de lancer la partie et de fermer la fnetre du menu
	def launch_game(self):
		# Etape de préparation pour voir si la grille séléctionné à des mots ou non
		if self.grille != "": # Si le joueur n'a pas choisi de Grille

			if glob.glob(f"mot/{self.grille}.txt") == []: # Si la grille n'a pas de mot
				# Affichage du label de l'erreur
				self.ERRORLABEL = CTkLabel(self, text = "La grille n'a pas de mots attitrés", text_color = "red", font = CTkFont(size = 15))
				self.ERRORLABEL.place(x = 100, y = 270)
				self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)
			else:
				self.destroy()
				Jeu(self.grille)
		else:
			self.ERRORLABEL = CTkLabel(self, text = "Veuillez choisir une grille", text_color = "red", font = CTkFont(size = 15))
			self.ERRORLABEL.place(x = 120, y = 270)
			self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)

	def go_creation(self):
		self.destroy()
		Creation()
	


# Classe de la fenetre de création de grille
class Creation(CTk):

	def __init__(self):
		super().__init__()

		self.title("Création de grilles") # Titre du jeu
		self.geometry("1200x700+300+150") # Dimmension de la fenetre
		#self.minsize(width = 1200, height = 700) # Dimmension minimum de la fenetre
		#self.maxsize(width = 1200, height = 700) # Dimmension maximale de la fenetre

		# Toutes les lettres de l'alphabet en majuscules
		self.letters = string.ascii_uppercase

		# Frame qui va contenir la grille et les options de création
		self.GrilleFrame = CTkFrame(self,width = 450, height = 660)
		self.GrilleFrame.grid(row = 0, column = 0, sticky = 'nwe', rowspan = 2, padx = 20, pady = 20)
		self.GrilleFrame.grid_propagate(0)

		# Double liste des entré qui vont prendre les lettre du joueur pour créer la grille
		self.entryGrille = [[CTkEntry(self.GrilleFrame,font = CTkFont(size = 25), width = 2, corner_radius = 10) for i in range(9)] for i in range(9)]
		# Double liste de charactère vide qui représente la grille que le joueur va créer
		self.nouvelleGrille = [["" for i in range(9)] for i in range(9)]
		# Liste des mots que le joueur veut ajouter
		self.listeMot = []
		
		# Frame qui va comporter l'entré pour le nom de la grille
		self.nomFrame = CTkFrame(self.GrilleFrame, height = 50)
		self.nomFrame.grid(row = 0, columnspan = 10, sticky = "nwe", padx = (20,0), pady = (10,0))
		self.nomFrame.grid_propagate(0)

		# Label qui précise où entrer le nom de la grille que le joueur veut générer
		self.nomLabel = CTkLabel(self.nomFrame, text = "Nom:", font = CTkFont(size = 15))
		self.nomLabel.grid(row = 0, column = 0, padx = (100,0), pady = (10,0))

		# Entry qui va prendre le nom de la grille que le joueur veut créer
		self.fileName = CTkEntry(self.nomFrame, font = CTkFont(size = 15))
		self.fileName.grid(row = 0, column = 1, padx = (10,0), pady = (10,0))
	
		# Bouton pour deséléctionné toutes les lettres
		self.ClearLettersBtn = CTkButton(self.GrilleFrame,text = "Clear",fg_color = "#337292", hover_color = "#4991B6",
		 font = CTkFont(size = 17), command = self.clear)
		self.ClearLettersBtn.grid(row = 11, column = 0,columnspan = 9)

		# Boutton pour creer des grilles
		self.CreationBoutton = CTkButton(self.GrilleFrame,text = "Générer",font = CTkFont(size = 17), fg_color = ("#3E9D44","#2C8031"),
		 hover_color = ("#2C8031","#3E9D44"), command = self.transformer)
		self.CreationBoutton.grid(padx = (10,0), row = 10, column = 0,columnspan = 9)

		# LabelFrame qui va comprendre la liste box des mots à trouver dans la grille
		self.MotATrouveFrame = CTkFrame(self, width = 250, height = 460)
		self.MotATrouveFrame.grid(row = 0,column = 1,padx = (0,20))
		self.MotATrouveFrame.grid_propagate(0)

		# Entrée qui va accueillir le mot que le joueur veut ajouter à sa liste
		self.MotEntry = CTkEntry(self.MotATrouveFrame, font = CTkFont(size = 25), width = 10)
		self.MotEntry.grid(row = 0, column = 0, columnspan = 2, sticky = 'ew', padx = (10,0), pady = (10,10))
		self.MotEntry.bind('<Return>',lambda event:self.add_mot())

		# Boutton pour retirer le mot sélectionné
		self.suppMot = CTkButton(self.MotATrouveFrame, text = "Supprimer", fg_color = ("#D7436D","#C22955"), hover_color = ("#C22955","#D7436D"),
			font = CTkFont(size = 17), command = self.supprimer_mot)
		self.suppMot.grid(row = 1, columnspan = 2, pady = (10,0))

		# List Box qui va comporter la liste de mots que le joueur doit trouver
		self.var = StringVar(value = self.listeMot)
		self.ListeBoxMotATrouver = Listbox(self.MotATrouveFrame, font = font.Font(size = 20), width = 13, height = 10,
			activestyle = 'none', selectbackground = "light grey", bg = "grey", fg = "white",
			borderwidth=0, highlightthickness=0, listvariable = self.var)
		self.ListeBoxMotATrouver.grid(columnspan = 2, row = 2, padx = (15,0), pady = 20, sticky = 'ew')

		# LabelFrame qui va contenir l'affichage de la grille généré par le joueur
		self.AffichageFrame = CTkFrame(self, width = 425, height = 660)
		self.AffichageFrame.grid(row = 0, column = 2, pady = 20, padx = (10,0))
		self.AffichageFrame.grid_propagate(0)

		# Frame on va apparaitre la grille
		self.GrilleFrame = CTkFrame(self.AffichageFrame, width = 400, height = 470)
		self.GrilleFrame.grid(row = 0, columnspan = 2, padx = (10,0), pady = 10)
		self.GrilleFrame.grid_propagate(0)

		# Double liste de Label qui vont représenté la grille du joueur lors de l'affichage
		self.lettreLabelListe = [[CTkLabel(self.GrilleFrame,font = CTkFont(size = 25), text = self.nouvelleGrille[x][y]) for y in range (9)] for x in range (9)]

		# Boutton pour enregistrer la grille généré en fichier txt ainsi que les mot
		self.SaveButton = CTkButton(self.AffichageFrame, text = "Enregistrer", fg_color = ("#755CA0","#644D8B"), hover_color = ("#644D8B","#755CA0"),
			font = CTkFont(size = 30), command = self.save_grille)
		self.SaveButton.grid(row = 1, column = 0, columnspan = 2, pady = (10,0))

		# Boutton pour revenir au menu
		self.leaveBtn = CTkButton(self.AffichageFrame, text="Revenir au Menu", fg_color = ("#D7436D","#C22955"), hover_color = ("#C22955","#D7436D"),
			command = self.back_menu, font = CTkFont(size=20))
		self.leaveBtn.grid(row = 2, column = 0, columnspan = 2, pady = (20,0))
		
		# Affichage des labels pour l'affichage des lettres de la grille
		r = 1
		for listeLabel in self.lettreLabelListe:
			c = 0
			for label in listeLabel:
				if c == 0:
					label.grid(row = r, column = c, padx = (27,0), pady = (20,0))
				else:
					label.grid(row = r, column = c, padx = (20,0), pady = (20,0))
				c += 1
			r += 1
		
		# Affichage de la grille d'entrée
		r = 1
		for listeEntry in self.entryGrille:
			c = 0
			for entry in listeEntry:
				if c == 0:
					entry.grid(row = r, column = c, padx = (20,0), pady = (10,0))
				else:
					entry.grid(row = r, column = c, padx = (10,0), pady = (10,0))
				c += 1
			r += 1

		self.mainloop()
		

	def back_menu(self):
		self.destroy()
		Menu()


	def save_grille(self):
		# vérification si un fichier existe déjà en ce nom
		liste_de_grille = glob.glob("grille/*.txt") # Liste des fichiers texte des grilles qui apparaissent dans le répértoire
		liste_de_mot = glob.glob("mot/*.txt") # Liste des fichier texte des mots qui apparaissent dans le répértoire
		fileName = self.fileName.get()

		if len(fileName) < 4: # Si la taille du nom de la grille est inférieur à 4
			# Label d'erreur
			self.ERRORLABEL = CTkLabel(self.AffichageFrame, text_color = ("#D7436D","#C22955"), font = CTkFont(size = 20),
				text = "Minimum 4 lettres dans le nom de la grille")
			self.ERRORLABEL.grid(row = 3, column = 0, columnspan = 2, pady = (20,0))					
			self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)
			return 1


		for i in range(len(liste_de_grille)):
			liste_de_grille[i] = liste_de_grille[i].replace('grille/','') # For ubuntu
			liste_de_grille[i] = liste_de_grille[i].replace('grille\\','') # For windows
			liste_de_grille[i] = liste_de_grille[i].replace('.txt','')

		for i in range(len(liste_de_mot)):
			if len(liste_de_mot) > 0:
				liste_de_mot[i] = liste_de_mot[i].replace('grille/','') # For ubuntu
				liste_de_mot[i] = liste_de_mot[i].replace('grille\\','') # For windows
				liste_de_mot[i] = liste_de_mot[i].replace('.txt','')

		if fileName not in liste_de_mot and fileName not in liste_de_grille: # Si le nom choisis par le joueur n'éxiste pas déjà
			if self.nouvelleGrille[0][0] != "" and len(self.listeMot) != 0: # Si l'une des deux liste est vide
				with open(f"grille/{fileName}.txt", 'w') as grilleFile: # On ouvre un nouveau fichier avec le nom
					for x in range(9):
						for y in range(9):
							if y == 8: # Si on arrive à la dernière lettre
								grilleFile.write(self.nouvelleGrille[x][y]) # écriture de la lettre dans le fichier 
							else: # Si on est pas à la dernière lettre
								grilleFile.write(self.nouvelleGrille[x][y]+',') # écriture de la lettre dans le fichier avec une virgule après
							
							self.nouvelleGrille[x][y] = ""
							self.lettreLabelListe[x][y].configure(text = "")

						grilleFile.writelines("\n")

				with open(f"mot/{fileName}.txt", 'w') as motFile: # Ouverture d'un nouveau fichier avec le nom de fichier du joueur
					for i in range(len(self.listeMot)-1,-1,-1): # pour chaque mots
						if i == 0: # Si on arrive au dernier mot
							motFile.write(self.listeMot[i]) # Écriture du mot sans virgule
						else:
							motFile.write(self.listeMot[i]+',') # Écriture du mot avec la virgule après
						self.listeMot.pop(i)
					self.var.set(self.listeMot)

			else:
				self.ERRORLABEL = CTkLabel(self.AffichageFrame,text_color = ("#D7436D","#C22955"), font = CTkFont(size = 20),
					text = "Générez une grille et ses mots d'abord !")
				self.ERRORLABEL.grid(row = 3, column = 0, columnspan = 2, pady = (20,0))
				self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)
		else:
			# Label d'erreur
			self.ERRORLABEL = CTkLabel(self.AffichageFrame, text_color = ("#D7436D","#C22955"), font = CTkFont(size = 18),
				text = "Une Grille ou liste de Mot éxiste déjà avec ce nom")
			self.ERRORLABEL.grid(row = 3, column = 0, columnspan = 2, pady = (20,0))
			self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)


	def supprimer_mot(self):
		
		try:
			self.listeMot.pop(self.ListeBoxMotATrouver.curselection()[0]) # On supprime de la liste le mot qui est selectionné dans la listBox
			self.var.set(self.listeMot) # On actualise la list box avec la nouvelle liste
		except: # Si on ne peut pas supprimer c'est que le joueur n'as pas sélectonné un mot dans la liste box
			# Label d'erreur
			self.ERRORLABEL = CTkLabel(self.GrilleFrame, text_color = ("#D7436D","#C22955"), font = CTkFont(size = 15),
				text = "Veuillez sélectionner un mot")
			self.ERRORLABEL.grid(row = 12, column = 0, columnspan = 2)
			self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)


	def add_mot(self):

		if len(self.listeMot) < 10: # Si la list box n'as pas plus de 10 mots
			if not self.space(self.MotEntry) and not self.MotEntry.get() == "": # Si il n'ya pas de mots dans le
				self.listeMot.append(self.MotEntry.get()) # Ajout du mot dans la liste des mots
				self.MotEntry.delete(0,len(self.MotEntry.get())) # Suppression du mot de l'entrée
				self.var.set(self.listeMot) # Actualisation de la liste box avec la nouvelle liste
			else:
				# Label d'erreur
				self.ERRORLABEL = CTkLabel(self.GrilleFrame, text_color = ("#D7436D","#C22955"), font = CTkFont(size = 15),
					text = "Entrez un mot sans espaces")
				self.ERRORLABEL.grid(row = 12, column = 0, columnspan = 9)
				self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)

		else:
			# Label d'erreur
			self.ERRORLABEL = CTkLabel(self.GrilleFrame, text_color = ("#D7436D","#C22955"), font = CTkFont(size = 15),
				text = "Nombre maximum de 10 mots")
			self.ERRORLABEL.grid(row = 12, column = 0, columnspan = 9)
			self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)


	def space(self,entry): # Méthode qui renvoie True si il y un espace dans la chaine donner par l'entrée
		fileName = entry.get() # Récupération de la chaine de caractère
		indc = 0
		space = False

		while not space and indc < len(fileName): #Tant qu'il n'y a pas d'espace et qu'on a pas fini de parcourir la chaine
			space = fileName[indc] == " "
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
		
		if not self.space(self.fileName): # Si le nom ne comporte pas d'espaces
			if not self.plus_une_lettre(): # Si il y a qu'une seule lettre dans chaque entrèe

				fileName = self.fileName.get()
				for x in range(len(self.entryGrille)):
					for y in range(len(self.entryGrille[0])):
						if self.entryGrille[x][y].get() != "": # Si l'entrée n'est pas vide
							self.nouvelleGrille[x][y] = self.entryGrille[x][y].get().upper() # affectation de chaque lettre des entrèes dans la liste
						else:# Si l'entrèe est vide
							self.nouvelleGrille[x][y] = self.letters[random.randint(0,25)] # Ajout d'une lettre au aléatoire dans la liste
				self.affichage_grille()

			else:
				# Label d'erreur
				self.ERRORLABEL = Label(self.GrilleLabelFrame, bg = "#45458B", fg = "red", font = font.Font(size = 14),
					text = "Insérez qu'une seule lettre dans chaque case")
				self.ERRORLABEL.pack(side = BOTTOM, pady = 10)					
				self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)
		else:
			# Label d'erreur
			self.ERRORLABEL = Label(self.GrilleLabelFrame, bg = "#45458B", fg = "red", font = font.Font(size = 14),
				text = "Pas d'espaces dans le nom")
			self.ERRORLABEL.pack(side = BOTTOM, pady = 10)					
			self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)


# Class de la fenetre de jeu
class Jeu(CTk):

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

		print(f"etat validé: {self.isValid}, état cliqué: {self.isClicked}")

		if self.isClicked: # Si la lettre est déjà cliqué
			if not self.isValid: # Si la lettre n'est pas encore validé
				self.boutton.configure(bg = "#9090EE",activebackground="#A3A3FE") # On remet une couleur par défaut 
				self.isClicked = False # Elle devient plus cliqué
				self.mot.text = [self.mot.text[i] for i in range(len(self.mot.text)) if self != self.mot.text[i]] # On retire la lettre du mot
				self.MotLabel.configure(text = self.mot) # Affichage du mot en cours

			else: # Si la lettre est déjà validé
				self.isClicked = False # Elle devient plus cliqué
				self.mot.text = [self.mot.text[i] for i in range(len(self.mot.text)) if self != self.mot.text[i]] # On retire la lettre du mot
				self.MotLabel.configure(text = self.mot) # Affichage du mot en cours

		else: # Si la lettre est pas encore cliqué
			if not self.isValid: # Si la lettre n'est pas validé
				self.boutton.configure(bg = "#995AD1",activebackground="#995AD1") # On change sa couleur pour dire qu'elle est cliqué
				self.isClicked = True # Elle devient 
				self.mot.ajouter_Lettre(self) # On l'ajoute au mot
				self.MotLabel.configure(text = self.mot) # Affichage du mot en cours

			else: # Si la lettre est déjà validé
				self.isClicked = True # Elle devient 
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
			lettre.isClicked = False
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
