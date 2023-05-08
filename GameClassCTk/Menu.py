
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
import os

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
		self.liste_de_grille = glob.glob("grille/*.txt")
		self.grille = ""

		for i in range(len(self.liste_de_grille)):
			self.liste_de_grille[i] = self.liste_de_grille[i].replace('grille/','') # Ubuntu
			self.liste_de_grille[i] = self.liste_de_grille[i].replace('grille\\','') # Windows
			self.liste_de_grille[i] = self.liste_de_grille[i].replace('.txt','')

		# Frame qui va occuper tout le haut du menu et qui va comporter la phrase de Menu
		self.MenuFrame = CTkFrame(self,height = 75)
		self.MenuFrame.grid(row = 0, column = 0, columnspan = 2, sticky = 'we', pady = (10,0), padx = 10)
		# Label du menu
		self.MenuLabel = CTkLabel(self.MenuFrame, text = "Mot Mélé", font = CTkFont(size = 30))
		self.MenuLabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)

		# Boutton qui permet de fermer la fenetre du menu et de lancer le jeu
		self.GameButton = CTkButton(self,text = "JOUER", font = CTkFont(size = 25), 
			fg_color = ("#8177B4","#6E64A2"), hover_color = ("#6E64A2","#8177B4"), command = self.launch_game)
		self.GameButton.grid(pady = (0,20), row = 3, columnspan = 2)

		# Boutton pour supprimer la grille séléctionné
		self.suppGrille = CTkButton(self, text = "Supprimer", font = CTkFont(size = 20),
			fg_color = ("#D7436D","#C22955"), hover_color = ("#C22955","#D7436D"), command = self.delete_grille)
		self.suppGrille.grid(row = 2, column = 0)

		self.comboboxVar = customtkinter.StringVar(value = "Choisissez")
		# ComboBox qui va comporter les grilles que le joueur peut Charger
		self.GrilleComboBox = customtkinter.CTkComboBox(self, font = CTkFont(size = 18),
			variable = self.comboboxVar, command = self.select_grille, values = self.liste_de_grille)
		self.GrilleComboBox.grid(row = 1, column = 1, rowspan = 2)

		# Boutton pour accéder à la page de création de Grilles
		self.CreationBoutton = CTkButton(self,text = "Creer",font = CTkFont(size = 20), command = self.go_creation,
			fg_color = ("#448784","#3B706E"), hover_color = ("#3B706E","#448784")) #self.go_creation
		self.CreationBoutton.grid(row = 1,column = 0, pady = (20,0))

		# Label d'erreur
		self.ERRORLABEL = CTkLabel(self, text = "", text_color ="#C22955",
			font = CTkFont(size = 15))
		self.ERRORLABEL.grid(row = 4, columnspan = 2)

		# Configuration de l'adaptation de la page principale
		self.rowconfigure(1, weight = 1)
		self.rowconfigure(2, weight = 1)
		self.rowconfigure(3, weight = 1)
		self.columnconfigure(0, weight = 1)
		self.columnconfigure(1, weight = 1)

		self.mainloop()

	# Méthode pour supprimer la grille séléctionné
	def delete_grille(self):

		if self.grille == '':
			# Affichage du label de l'erreur
			self.ERRORLABEL.configure(text = "Veuillez choisir une grille", text_color = "#C22955")
			self.ERRORLABEL.after(3000,self.clear_error_message)
			return 1

		MessageBox(self.grille, self)


	# Meéthode qui supprime le texte du label d'erreur
	def clear_error_message(self):
		self.ERRORLABEL.configure(text = "")

	# Méthode qui actualise la grille sélectionné
	def select_grille(self,choice):
		self.grille = choice

	# Méthode qui va servir de lancer la partie et de fermer la fnetre du menu
	def launch_game(self):
		# Etape de préparation pour voir si la grille séléctionné à des mots ou non
		if self.grille != "": # Si le joueur n'a pas choisi de Grille

			if glob.glob(f"mot/{self.grille}.txt") == []: # Si la grille n'a pas de mot
				# Affichage du label de l'erreur
				self.ERRORLABEL.configure(text = "La grille n'a pas de mots attitrés", text_color = "#C22955") 
				self.ERRORLABEL.after(3000,self.clear_error_message)
			else:
				self.destroy()
				Jeu.Jeu(self.grille)
		else:
			self.ERRORLABEL.configure(text = "Veuillez choisir une grille", text_color = "#C22955")
			self.ERRORLABEL.after(3000,self.clear_error_message)

	# Méthode qui lance la fenetre de création de grille
	def go_creation(self):
		self.destroy()
		Creation.Creation()


class MessageBox(CTk):
	
	def __init__(self, grille, jeu):
		super().__init__()

		self.title("Quitter") # Titre de la fenetre
		self.geometry("400x300+850+300") # Dimmension de la fenetre
		self.minsize(width = 300, height = 150)
		self.maxsize(width = 300, height = 150)

		self.jeu = jeu

		# Text qui demande au joueur s'il veut quitter le jeu
		self.label = CTkLabel(self, text = "Voulez-vous supprimer la grille ?", font = CTkFont(size = 20))
		self.label.grid(row = 0, column = 0, columnspan = 2)

		# Bouton de réponse du joueur
		## rester sur le jeu
		self.No = CTkButton(self, text = "Non", font = CTkFont(size = 20),
			fg_color = "#2C8031", hover_color = "#3E9D44",
			command = self.leave)
		self.No.grid(row = 1, column = 0)

		self.yes = CTkButton(self, text = "Oui", font = CTkFont(size = 20),
			fg_color = "#C22955", hover_color = "#D7436D",
			command = self.delete)
		self.yes.grid(row = 1, column = 1)


		# Centrage des éléments de la fenetre
		self.columnconfigure(1, weight = 1)
		self.columnconfigure(2, weight = 1)
		self.rowconfigure(1, weight = 2)
		self.rowconfigure(2, weight = 1)

		
		self.mainloop()

	# Méthode pour quitter la fenetre
	def delete(self):
		try: # Suppression du fichier choisis
			os.remove(f'grille/{self.jeu.grille}.txt')
			os.remove(f'mot/{self.jeu.grille}.txt')

			# Actualisation de la comboBox
			self.delete_grille_liste()
			self.jeu.GrilleComboBox.configure(values = self.jeu.liste_de_grille)
			self.jeu.GrilleComboBox.set("Choisissez")

		except FileNotFoundError: # Exception si le fichier existe plus
			self.jeu.ERRORLABEL.configure(text = "La grille n'existe plus", text_color = "#C22955")
			self.jeu.ERRORLABEL.after(3000,self.jeu.clear_error_message)

		else: # Sinon 
			self.jeu.ERRORLABEL.configure(text = "Grille supprimé", text_color = "#459359")
			self.jeu.ERRORLABEL.after(3000,self.jeu.clear_error_message)

		self.destroy()

	def delete_grille_liste(self):

		indG = 0
		trouve = False

		while not trouve and indG < len(self.jeu.liste_de_grille):
			trouve = self.jeu.liste_de_grille[indG] == self.jeu.grille
			indG += 1

		if trouve:
			self.jeu.liste_de_grille.pop(indG-1)


	# Méthode pour annuler la suppression
	def leave(self):
		self.destroy()


		


		