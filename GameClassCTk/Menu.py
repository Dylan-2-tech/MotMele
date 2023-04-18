
#### Importation des librairies ####
import customtkinter
from customtkinter import CTk
from customtkinter import CTkButton
from customtkinter import CTkFont
from customtkinter import CTkFrame
from customtkinter import CTkLabel
from tkinter import CENTER
import string
import glob
import GameClassCTk.Jeu as Jeu
import GameClassCTk.Creation as Creation
import time

customtkinter.set_appearance_mode("dark") # Thème général de l'application (dark, light, system)

# Class menu pour la personnalisation du jeu et lancement du jeu
class Menu(CTk):

	def __init__(self):
		super().__init__()
		self.title("Menu") # Titre du jeu
		self.geometry("400x300+800+250") # Dimmension de la fenetre
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
		self.MenuFrame.grid(row = 0, column = 0, columnspan = 2, sticky = 'we', pady = (10,0), padx = 10)
		# Label du menu
		self.MenuLabel = CTkLabel(self.MenuFrame, text = "Mot Mélé", font = CTkFont(size = 30))
		self.MenuLabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)

		# Boutton qui permet de fermer la fenetre du menu et de lancer le jeu
		self.GameButton = CTkButton(self,text = "JOUER", font = CTkFont(size = 25), 
			fg_color = ("#8177B4","#6E64A2"), hover_color = ("#6E64A2","#8177B4"), command = self.launch_game)
		self.GameButton.grid(row = 1,column = 0)

		comboboxVar = customtkinter.StringVar(value = "Choisissez")
		# ComboBox qui va comporter les grilles que le joueur peut Charger
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

		self.mainloop()


	# Méthode qui actalise la grille sélectionné
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
				Jeu.Jeu(self.grille)
		else:
			self.ERRORLABEL = CTkLabel(self, text = "Veuillez choisir une grille", text_color = "red", font = CTkFont(size = 15))
			self.ERRORLABEL.place(x = 120, y = 270)
			self.ERRORLABEL.after(3000,self.ERRORLABEL.destroy)

	# Méthode qui lance la fenetre de création de grille
	def go_creation(self):
		self.destroy()
		Creation.Creation()