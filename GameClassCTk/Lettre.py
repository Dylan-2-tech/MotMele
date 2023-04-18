
#### Importation des librairie ####
import customtkinter
from customtkinter import CTkButton
from customtkinter import CTkFont

customtkinter.set_appearance_mode("dark") # Thème général de l'application (dark, light, system)


# Class des lettres
class Lettre():

	def __init__(self,lettre,x,y,game):

		self.MotLabel = game.MotLabel
		self.mot = game.mot
		self.isClicked = False
		self.x = x # position x de la lettre
		self.y = y # position y de la lettre
		self.lettre = lettre
		self.boutton = CTkButton(game.GrilleFrame, text = "".join(lettre),
		 	font = CTkFont(size=35), command=self.clicked, border_width = 5, border_color = ("#8880A9","#514683"),
		 	fg_color = ("#9287C7","#5F5591"), hover_color = ("#BCB3E4","#746AA4"))

	# méthode qui s'active quand la lettre est cliqué
	def clicked(self):

		if self.isClicked: # Si la lettre est déjà cliqué
			self.boutton.configure(fg_color = ("#9287C7","#5F5591"), 
				hover_color = ("#BCB3E4","#746AA4")) # On remet une couleur par défaut 
			self.isClicked = False # Elle devient plus cliqué
			self.mot.supprimer_Lettre(self)
			self.MotLabel.configure(text = self.mot) # Affichage du mot en cours
		
		else: # Si la lettre est pas encore cliqué
			self.boutton.configure(fg_color = ("#AB86C5","#785591"), 
				hover_color = ("#C5A9DA","#996EB8")) # On change sa couleur pour dire qu'elle est cliqué
			self.isClicked = True # Elle devient cliqué
			self.mot.ajouter_Lettre(self) # On l'ajoute au mot
			self.MotLabel.configure(text = self.mot) # Affichage du mot en cours