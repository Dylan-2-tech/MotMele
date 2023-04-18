
#### Importation des librairie ####
import customtkinter
from customtkinter import CTk
from customtkinter import CTkButton
from customtkinter import CTkFont
from customtkinter import CTkFrame
from customtkinter import CTkLabel
from customtkinter import CTkEntry
from customtkinter import CTkRadioButton
from customtkinter import IntVar
from tkinter import CENTER
from tkinter import Listbox
from tkinter import StringVar
from tkinter import font
import random
import string
import glob
import GameClassCTk.Menu as Menu

customtkinter.set_appearance_mode("dark") # Thème général de l'application (dark, light, system)


# Classe de la fenetre de création de grille
class Creation(CTk):

	def __init__(self):
		super().__init__()

		self.title("Création de grilles") # Titre du jeu
		self.geometry("1200x700+300+150") # Dimmension de la fenetre
		self.minsize(width = 1200, height = 700) # Dimmension minimum de la fenetre
		self.maxsize(width = 1200, height = 700) # Dimmension maximale de la fenetre

		# Si diff == 1 (facile) et 2 (difficile)
		self.diff = IntVar()

		# Frame qui va contenir la grille et les options de création
		self.GrilleFrame = CTkFrame(self,width = 450, height = 660)
		self.GrilleFrame.grid(row = 0, column = 0, sticky = 'nwes', rowspan = 2, padx = 20, pady = 20)
		self.GrilleFrame.grid_propagate(0)

		# Double liste des entrés qui vont prendre les lettres du joueur pour créer la grille
		self.entryGrille = [[CTkEntry(self.GrilleFrame,font = CTkFont(size = 25), width = 2, corner_radius = 10) for i in range(9)] for i in range(9)]
		# Double liste de charactères vide qui représente la grille que le joueur va créer
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

		# Entré qui va prendre le nom de la grille que le joueur veut créer
		self.fileName = CTkEntry(self.nomFrame, font = CTkFont(size = 15))
		self.fileName.grid(row = 0, column = 1, padx = (10,0), pady = (10,0))

		# Boutton pour creer des grilles
		self.CreationBoutton = CTkButton(self.GrilleFrame,text = "Générer",font = CTkFont(size = 25), fg_color = ("#3E9D44","#2C8031"),
		 hover_color = ("#2C8031","#3E9D44"), command = self.generer)
		self.CreationBoutton.grid(row = 10, pady = (20,10), column = 0,columnspan = 5)
	
		# Boutton pour deséléctionné toutes les lettres de la grille
		self.ClearLettersBtn = CTkButton(self.GrilleFrame,text = "Clear",fg_color = "#337292", hover_color = "#4991B6",
		 font = CTkFont(size = 25), command = self.clear)
		self.ClearLettersBtn.grid(row = 11, pady = (10,20), column = 0, columnspan = 5)

		# Boutton radio de difficulté facile
		self.EazyRadioButton = CTkRadioButton(self.GrilleFrame, text = "Facile",
			font = CTkFont(size = 20), hover_color = "#459359", border_color = "#459359",
			variable = self.diff, value = 1)
		self.EazyRadioButton.grid(row = 10, column = 4, columnspan = 5)

		# Boutton radio de difficulté difficile
		self.HardRadioButton = CTkRadioButton(self.GrilleFrame, text = "Difficile",
			font = CTkFont(size = 20), hover_color = "#C22955", border_color = "#C22955",
			variable = self.diff, value = 2)
		self.HardRadioButton.grid(row = 11, column = 4, columnspan = 5)

		# Frame qui va comprendre la liste box des mots à trouver dans la grille
		self.MotATrouveFrame = CTkFrame(self, width = 250, height = 460)
		self.MotATrouveFrame.grid(row = 0,column = 1,padx = (0,20))
		self.MotATrouveFrame.grid_propagate(0)

		# Entrée qui va accueillir le mot que le joueur veut ajouter à sa liste
		self.MotEntry = CTkEntry(self.MotATrouveFrame, font = CTkFont(size = 30), width = 10)
		self.MotEntry.grid(row = 0, column = 0, columnspan = 2, sticky = 'ew', pady = (10,10), padx = (20,0) )
		self.MotEntry.bind('<Return>',lambda event:self.add_mot())

		# Boutton pour retirer le mot sélectionné
		self.suppMot = CTkButton(self.MotATrouveFrame, text = "Supprimer", fg_color = ("#D7436D","#C22955"), hover_color = ("#C22955","#D7436D"),
			font = CTkFont(size = 17), command = self.supprimer_mot)
		self.suppMot.grid(row = 1, column = 0, columnspan = 2, pady = (10,0), padx = (20,0))

		# List Box qui va comporter la liste de mots que le joueur doit trouver
		self.var = StringVar(value = self.listeMot)
		self.ListeBoxMotATrouver = Listbox(self.MotATrouveFrame, font = font.Font(size = 20), width = 14, height = 10,
			activestyle = 'none', selectbackground = "#525252", bg = "#3C3C3C", fg = "white",
			borderwidth=0, highlightthickness=0, listvariable = self.var)
		self.ListeBoxMotATrouver.grid(column = 0, row = 2, columnspan = 2, padx = (20,0), pady = 20, sticky = 'ew')

		# Frame qui va contenir l'affichage de la grille généré par le joueur
		self.AffichageFrame = CTkFrame(self, width = 425, height = 660)
		self.AffichageFrame.grid(row = 0, column = 2, pady = 20, sticky = 'we')
		self.AffichageFrame.grid_propagate(0)

		# Frame où va apparaitre la grille
		self.GrilleAffichageFrame = CTkFrame(self.AffichageFrame, width = 400, height = 470)
		self.GrilleAffichageFrame.grid(row = 0, columnspan = 2, padx = (10,0), pady = 10)
		self.GrilleAffichageFrame.grid_propagate(0)

		# Double liste de Label qui vont représenté la grille du joueur lors de l'affichage
		self.lettreLabelListe = [[CTkLabel(self.GrilleAffichageFrame,font = CTkFont(size = 25), text = self.nouvelleGrille[x][y]) for y in range (9)] for x in range (9)]

		# Boutton pour enregistrer la grille généré en fichier txt ainsi que les mot
		self.SaveButton = CTkButton(self.AffichageFrame, text = "Enregistrer", fg_color = ("#755CA0","#644D8B"), hover_color = ("#644D8B","#755CA0"),
			font = CTkFont(size = 30), command = self.save_grille)
		self.SaveButton.grid(row = 1, column = 0, columnspan = 2, pady = (10,0))

		# Boutton pour revenir au menu
		self.leaveBtn = CTkButton(self.AffichageFrame, text="Revenir au Menu", fg_color = ("#D7436D","#C22955"), hover_color = ("#C22955","#D7436D"),
			command = self.back_menu, font = CTkFont(size=20))
		self.leaveBtn.grid(row = 2, column = 0, columnspan = 2, pady = (20,0))

		# Label d'erreur de l'affichage
		self.ERRORLABEL_AFFICHAGE = CTkLabel(self.AffichageFrame, text_color = "#C22955", font = CTkFont(size = 20),
			text = "")
		self.ERRORLABEL_AFFICHAGE.grid(row = 3, column = 0, columnspan = 2, pady = (20,0))

		# Label d'erreur de la grille
		self.ERRORLABEL_GRILLE = CTkLabel(self.GrilleFrame, font = CTkFont(size = 20),
			text = "")
		self.ERRORLABEL_GRILLE.grid(row = 12, column = 0, columnspan = 9)


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

	# Méthode de retour vers le menu
	def back_menu(self):
		self.destroy()
		Menu.Menu()

	# Méthode qui efface les erreurs
	def clear_error_message(self):
		self.ERRORLABEL_GRILLE.configure(text = "")
		self.ERRORLABEL_AFFICHAGE.configure(text = "")
	
	# Méthode qui enregistre la grille créée en format txt
	def save_grille(self):
		# vérification si un fichier existe déjà en ce nom
		liste_de_grille = glob.glob("grille/*.txt") # Liste des fichiers texte des grilles qui apparaissent dans le répértoire
		liste_de_mot = glob.glob("mot/*.txt") # Liste des fichier texte des mots qui apparaissent dans le répértoire
		fileName = self.fileName.get()

		if len(fileName) < 4: # Si la taille du nom de la grille est inférieur à 4
			# Label d'erreur
			self.ERRORLABEL_GRILLE.configure(text_color = "#C22955", text = "Minimum 4 lettres dans le nom de fichier")
			self.ERRORLABEL_GRILLE.after(3000,self.clear_error_message)
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

				self.ERRORLABEL_AFFICHAGE.configure(text_color = "#459359", text = "Grille créé")
				self.ERRORLABEL_AFFICHAGE.after(3000,self.clear_error_message)

			else:
				self.ERRORLABEL_AFFICHAGE.configure(text_color = "#C22955", text = "Générez une grille et ses mots d'abord !")
				self.ERRORLABEL_AFFICHAGE.after(3000,self.clear_error_message)
		else:
			# Label d'erreur
			self.ERRORLABEL_AFFICHAGE.configure(text_color = "#C22955", text = "Une Grille ou liste de Mot éxiste déjà avec ce nom")
			self.ERRORLABEL_AFFICHAGE.after(3000,self.clear_error_message)


	# Méthode qui supprime le mot sélectionné
	def supprimer_mot(self):
		
		try:
			self.listeMot.pop(self.ListeBoxMotATrouver.curselection()[0]) # On supprime de la liste le mot qui est selectionné dans la listBox
			self.var.set(self.listeMot) # On actualise la list box avec la nouvelle liste
		except: # Si on ne peut pas supprimer c'est que le joueur n'as pas sélectonné un mot dans la liste box
			# Label d'erreur
			self.ERRORLABEL_GRILLE.configure(text_color = "#C22955", text = "Veuillez sélectionner un mot")
			self.ERRORLABEL_GRILLE.after(3000,self.clear_error_message)


	# Méthode qui ajoute le mot quand l'utilisateur appuie sur entrée
	def add_mot(self):

		### Toutes les conditions
		newWord = self.MotEntry.get() not in self.listeMot # Vrai si le mot est déjà dans la liste
		btw410 = len(self.MotEntry.get()) <= 9 and len(self.MotEntry.get()) >= 5 # Vrai si la taille ne dépasse pas 9 lettres
		minLength = len(self.listeMot) < 10 # Vrai Si la list box n'as pas plus de 10 mots
		spaceOrEmpty = not self.space(self.MotEntry) and not self.MotEntry.get() == "" # Si aucun mot saisi ou espace dans le mot

		if newWord:
			if btw410:
				if minLength:
					if spaceOrEmpty:
						self.listeMot.append(self.MotEntry.get()) # Ajout du mot dans la liste des mots
						self.MotEntry.delete(0,len(self.MotEntry.get())) # Suppression du mot de l'entrée
						self.var.set(self.listeMot) # Actualisation de la liste box avec la nouvelle liste
					else:
						# Label d'erreur
						self.ERRORLABEL_GRILLE.configure(text_color = "#C22955", text = "Entrez un mot sans espaces")
						self.ERRORLABEL_GRILLE.after(3000,self.clear_error_message)

				else:
					# Label d'erreur
					self.ERRORLABEL_GRILLE.configure(text_color = "#C22955", text = "Nombre maximum de 10 mots")
					self.ERRORLABEL_GRILLE.after(3000,self.clear_error_message)
			else:
				# Label d'erreur
				self.ERRORLABEL_GRILLE.configure(text_color = "#C22955", text = "Nombre de lettres entre 5 et 9")
				self.ERRORLABEL_GRILLE.after(3000,self.clear_error_message)
		else:
			self.ERRORLABEL_GRILLE.configure(text_color = "#C22955", text = f"{self.MotEntry.get()} existe déjà")
			self.ERRORLABEL_GRILLE.after(3000,self.clear_error_message)

	# Méthode qui renvoie True si il y a des espaces dans le l'entrée en parametre
	def space(self,entry): # Méthode qui renvoie True si il y un espace dans la chaine donner par l'entrée
		text = entry.get() # Récupération de la chaine de caractère
		indc = 0
		space = False

		while not space and indc < len(text): #Tant qu'il n'y a pas d'espace et qu'on a pas fini de parcourir la chaine
			space = text[indc] == " "
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
	def generer(self):

		# Si aucune difficulté est choisie
		if self.diff.get() == 0:
			self.ERRORLABEL_GRILLE.configure(text_color = "#C22955", text = "Séléctionnez une difficulté")
			self.ERRORLABEL_GRILLE.after(3000,self.clear_error_message)
			return 1 # Quitter la méthode

		# Si la difficulté facile est choisie et qu'il y a 5 mots minimum 
		elif self.diff.get() == 1 and len(self.listeMot) > 4:
			lettres = string.ascii_uppercase
		
		# Si la difficulté difficile est choisie et qu'il y a 5 mots minimum 
		elif self.diff.get() == 2 and len(self.listeMot) > 4:
			lettres = []
			for mot in self.listeMot:
				for cara in mot:
					if cara not in lettres:
						lettres.append(cara.upper())
		
		# S'il n'y a pas de minimu 5 mots
		else:
			self.ERRORLABEL_GRILLE.configure(text_color = "#C22955", text = "Entrez au moins 5 mots")
			self.ERRORLABEL_GRILLE.after(3000,self.clear_error_message)
			return 1 # Quitter la méthode

		if not self.space(self.fileName): # Si le nom ne comporte pas d'espaces
			if not self.plus_une_lettre(): # Si il y a qu'une seule lettre dans chaque entrèe

				fileName = self.fileName.get()
				for x in range(len(self.entryGrille)):
					for y in range(len(self.entryGrille[0])):
						if self.entryGrille[x][y].get() != "": # Si l'entrée n'est pas vide
							self.nouvelleGrille[x][y] = self.entryGrille[x][y].get().upper() # affectation de chaque lettre des entrèes dans la liste
						else:# Si l'entrèe est vide
							self.nouvelleGrille[x][y] = lettres[random.randint(0,len(lettres)-1)] # Ajout d'une lettre au aléatoire dans la liste
				self.affichage_grille()

			else:
				# Label d'erreur
				self.ERRORLABEL_GRILLE.configure(text_color = "#C22955", text = "Insérez qu'une seule lettre dans chaque case")
				self.ERRORLABEL_GRILLE.after(3000,self.clear_error_message)
		else:
			# Label d'erreur
			self.ERRORLABEL_GRILLE.configure(text_color = "#C22955", text = "Pas d'espaces dans le nom")
			self.ERRORLABEL_GRILLE.after(3000,self.clear_error_message)
