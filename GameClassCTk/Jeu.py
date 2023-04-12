
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

customtkinter.set_appearance_mode("dark") # Thème général de l'application (dark, light, system)

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

		# Frame qui va comporter la grille de jeu
		self.GrilleFrame = CTkFrame(self)
		self.GrilleFrame.grid(sticky = 'ewns', column = 0, row = 0, pady = 20, padx = 20)
		self.GrilleFrame.grid_propagate(0)

		# Frame qui va comporter tout les boutons pour valider etc
		self.GameFrame = CTkFrame(self)
		self.GameFrame.grid(sticky = 'ensw', column = 1, row = 0, padx = (0,20), pady = 20)
		self.GameFrame.grid_propagate(0)

		self.columnconfigure(0, weight = 2)
		self.columnconfigure(1, weight = 1)
		self.rowconfigure(0, weight = 1)

		self.GrilleFrame.columnconfigure(0, weight = 1)
		self.GrilleFrame.columnconfigure(1, weight = 1)
		self.GrilleFrame.columnconfigure(2, weight = 1)
		self.GrilleFrame.columnconfigure(3, weight = 1)
		self.GrilleFrame.columnconfigure(4, weight = 1)
		self.GrilleFrame.columnconfigure(5, weight = 1)
		self.GrilleFrame.columnconfigure(6, weight = 1)
		self.GrilleFrame.columnconfigure(7, weight = 1)
		self.GrilleFrame.columnconfigure(8, weight = 1)

		self.GrilleFrame.rowconfigure(0, weight = 1)
		self.GrilleFrame.rowconfigure(1, weight = 1)
		self.GrilleFrame.rowconfigure(2, weight = 1)
		self.GrilleFrame.rowconfigure(3, weight = 1)
		self.GrilleFrame.rowconfigure(4, weight = 1)
		self.GrilleFrame.rowconfigure(5, weight = 1)
		self.GrilleFrame.rowconfigure(6, weight = 1)
		self.GrilleFrame.rowconfigure(7, weight = 1)
		self.GrilleFrame.rowconfigure(8, weight = 1)

		"""


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
		"""


		# génération de la map des lettres
		for x in range(len(self.grille)):
			for y in range(len(self.grille[0])):
				lettre = Lettre(self.grille[x][y].upper(),x,y,self) # on initialise les lettre grâce à la classe Lettre
				self.grille[x][y] = lettre
				lettre.boutton.grid(row = x, column = y, padx = (15,0), pady = (15,0), sticky = 'ensw')


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