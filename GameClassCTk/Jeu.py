
#### Importation des librairie ####
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
import string
import glob
from GameClassCTk.Lettre import Lettre
from GameClassCTk.Mot import Mot
import GameClassCTk.Menu as Menu

customtkinter.set_appearance_mode("dark") # Thème général de l'application (dark, light, system)

# Class de la fenetre de jeu
class Jeu(CTk):

	def __init__(self,grille):
		super().__init__()

		# Initialisation de la fenetre du jeu
		self.title("Mot Mélé") # Titre du jeu
		self.geometry("1200x735+350+150") # Dimmension de la fenetre
		self.minsize(width = 1200, height = 735) # Dimmension minimum de la fenetre


		# Grille du jeu
		self.grille = [line.split(',') for line  in open(f"grille/{grille}.txt")]
		for listLettre in self.grille:
			for i in range(len(listLettre)):
				listLettre[i] = listLettre[i].replace('\n','')

		# Liste des mots à trouver
		self.listeMot = [mot.upper().split(',') for mot in open(f"mot/{grille}.txt")][0]
		self.listeMotTrouve = [] # Liste des mot déjà trouvé


		# Frame qui va comporter la grille de jeu
		self.GrilleFrame = CTkFrame(self)
		self.GrilleFrame.grid(sticky = 'ewns', column = 0, row = 0, pady = 20, padx = 20)
		self.GrilleFrame.grid_propagate(0)

		# Frame qui va comporter tout les bouttons pour valider etc
		self.GameFrame = CTkFrame(self)
		self.GameFrame.grid(sticky = 'ensw', column = 1, row = 0, padx = (0,20), pady = 20)
		self.GameFrame.grid_propagate(0)

		# Frame qui va contenir le label qui affiche le mot
		self.MotFrame = CTkFrame(self.GameFrame)
		self.MotFrame.grid(row = 0, column = 0, columnspan = 2, sticky = 'we', padx = 30)

		# Label qui affiche le mot séléctionné
		self.MotLabel = CTkLabel(self.MotFrame, font = CTkFont(size=40), text = "")#,fg_color = ("","")
		self.MotLabel.grid(padx = 20, pady = 15)

		# Boutton pour valider la sélection des lettres
		self.valideBtn = CTkButton(self.GameFrame, text = "Valider",fg_color = "#2C8031", hover_color = "#3E9D44", 
			font = CTkFont(size = 30), command = self.valider)
		self.valideBtn.grid(row = 1, column = 0)

		# Bouton pour deséléctionné toutes les lettres
		self.ClearLettersBtn = CTkButton(self.GameFrame, text = "Clear", fg_color = "#337292", hover_color = "#4991B6",
			font = CTkFont(size = 30) , command = self.clear)
		self.ClearLettersBtn.grid(row = 1, column = 1)

		# Label qui va prendre en son intérieur les mots à trouver
		self.MotATrouveFrame = CTkFrame(self.GameFrame)
		self.MotATrouveFrame.grid(row = 2, column = 0, columnspan = 2)

		# ListBox qui va afficher les mots à trouvé
		self.var = StringVar(value = self.listeMot)
		self.ListeBoxMotATrouver = Listbox(self.MotATrouveFrame,
			font = font.Font(size = 20), width = 16, activestyle = 'none',
			selectbackground = "#525252", bg = "#3C3C3C", borderwidth=0,
			highlightthickness=0, listvariable = self.var, fg = "white")
		self.ListeBoxMotATrouver.grid(sticky = 'ensw', columnspan = 2)

		# Boutton pour revenir au menu
		self.leaveBtn = CTkButton(self.GameFrame, text = "Revenir au Menu",
			fg_color = "#C22955", hover_color = "#D7436D", command = self.back_menu,
			font = CTkFont(size = 25))
		self.leaveBtn.grid(row = 3, column = 0, columnspan = 2)

		# Label d'erreur
		self.ERRORLABEL = CTkLabel(self.GameFrame, font = CTkFont(size = 25),
			text = "")
		self.ERRORLABEL.grid(row = 4, column = 0, columnspan = 2)

		# Mot qui va changer au fur et à mesure de la partie
		self.mot = Mot()

		# génération de la map des lettres
		for x in range(len(self.grille)):
			for y in range(len(self.grille[0])):
				lettre = Lettre(self.grille[x][y].upper(),x,y,self) # on initialise les lettre grâce à la classe Lettre
				self.grille[x][y] = lettre
				lettre.boutton.grid(row = x, column = y, padx = 5, pady = 5, sticky = 'ensw')

		# Allignement principale des 2 columns, 0 = GrilleFrame et 1 = GameFrame
		self.columnconfigure(0, weight = 2)
		self.columnconfigure(1, weight = 1)
		self.rowconfigure(0, weight = 1)

		# Allignement vertical des lettres
		self.GrilleFrame.columnconfigure(0, weight = 1)
		self.GrilleFrame.columnconfigure(1, weight = 1)
		self.GrilleFrame.columnconfigure(2, weight = 1)
		self.GrilleFrame.columnconfigure(3, weight = 1)
		self.GrilleFrame.columnconfigure(4, weight = 1)
		self.GrilleFrame.columnconfigure(5, weight = 1)
		self.GrilleFrame.columnconfigure(6, weight = 1)
		self.GrilleFrame.columnconfigure(7, weight = 1)
		self.GrilleFrame.columnconfigure(8, weight = 1)

		# Allignement horizontale des lettres
		self.GrilleFrame.rowconfigure(0, weight = 1)
		self.GrilleFrame.rowconfigure(1, weight = 1)
		self.GrilleFrame.rowconfigure(2, weight = 1)
		self.GrilleFrame.rowconfigure(3, weight = 1)
		self.GrilleFrame.rowconfigure(4, weight = 1)
		self.GrilleFrame.rowconfigure(5, weight = 1)
		self.GrilleFrame.rowconfigure(6, weight = 1)
		self.GrilleFrame.rowconfigure(7, weight = 1)
		self.GrilleFrame.rowconfigure(8, weight = 1)

		# Allignement des bouton dans la GameFrame
		self.GameFrame.columnconfigure(0, weight = 1)
		self.GameFrame.columnconfigure(1, weight = 1)
		self.GameFrame.rowconfigure(0, weight = 1)
		self.GameFrame.rowconfigure(1, weight = 1)
		self.GameFrame.rowconfigure(2, weight = 1)
		self.GameFrame.rowconfigure(3, weight = 2)
		self.GameFrame.rowconfigure(4, weight = 1)

		# Centrage du label du mot
		self.MotFrame.rowconfigure(0, weight = 1)
		self.MotFrame.columnconfigure(0, weight = 1)

		self.mainloop() # Affichage de la fenetre


	# Méthode qui nettoie les lettres sélectionner mais pas validé
	def clear(self):
		self.mot.clear_mot()
		self.MotLabel.configure(text = self.mot.get_mot())
		for listeLettre in self.grille:
			for lettre in listeLettre:
				if lettre.isClicked:
					lettre.isClicked = False
					lettre.boutton.configure(fg_color = ("#9287C7","#5F5591"), 
						hover_color = ("#BCB3E4","#746AA4"))

	# Méthode qui efface le texte des erreurs
	def clear_error_message(self):
		self.ERRORLABEL.configure(text = "")

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
					self.ERRORLABEL.configure(text_color = "#459359", text = "Gagné !")
					self.ERRORLABEL.after(3000,self.clear_error_message)
					# arreter le timer
				else:
					self.ERRORLABEL.configure(text_color = "#459359", text = "Vous avez trouvé le mot !")
					self.ERRORLABEL.after(3000,self.clear_error_message)
				
			elif mot in self.listeMotTrouve: # Si le mot est déjà trouvé
				self.ERRORLABEL.configure(text_color = "#D31842", text = "Mot déjà trouvé")
				self.ERRORLABEL.after(3000,self.clear_error_message)

			else: # Si le mot n'est pas le bon
				self.ERRORLABEL.configure(text_color = "#D31842", text = "Pas le bon mot :/")
				self.ERRORLABEL.after(3000,self.clear_error_message)

		else: # Si le mot n'est pas correct
			self.ERRORLABEL.configure(text_color = "#D31842", text = "Le mot n'est pas valide")
			self.ERRORLABEL.after(3000,self.clear_error_message)

		self.mot.clear_mot()
		self.clear()

	# Méthode qui reviens au menu
	def back_menu(self):
		self.destroy()
		Menu.Menu()