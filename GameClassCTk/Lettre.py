
#### Importation des librairie ####
import customtkinter
from customtkinter import CTkButton
from customtkinter import CTkFont

customtkinter.set_appearance_mode("dark") # Thème général de l'application (dark, light, system)


# Class des lettres
class Lettre():

	def __init__(self,lettre,x,y,game):

		#self.MotLabel = game.MotLabel
		#self.mot = game.mot
		self.isValid = False # Si le mot est validé
		self.isClicked = False # Si il est cliqué alors
		self.x = x # position x de la lettre
		self.y = y # position y de la lettre
		self.lettre = lettre
		self.boutton = CTkButton(game.GrilleFrame, text = "".join(lettre),
		 	font = CTkFont(size=35), command=self.clicked) #, width = 50, height = 50
	
	def clicked(self): # méthode qui s'active quand la lettre est cliqué

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
