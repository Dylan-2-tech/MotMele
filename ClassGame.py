from tkinter import *
from tkinter import ttk
import tkinter.font as font

#### Fichier des class du jeu ####

# Class De la fenetre de jeu
class Jeu:

	def __init__(self):
		# C'est la map qui contiendras les lettres
		self.gameMap = [ ["A","B","G","N","I","Z","Y","I"],
					["B","H","Y","A","W","Q","U","A"],
					["H","R","D","T","P","O","V","W"],
					["L","J","G","Z","I","M","R","F"],
					["E","X","B","N","K","M","T","Y"],
					["X","T","S","L","G","Y","H","O"]]


		# Initialisation de la fenetre du jeu
		gameWindow = Tk()
		gameWindow.title("Mot Croisé") # Titre du jeu
		gameWindow.geometry("1000x500+400+250") # Dimmension de la fenetre
		gameWindow.minsize(width = 1000, height = 500) # Dimmension minimum de la fenetre
		gameWindow.maxsize(width = 1000, height = 500) # Dimmension maximale de la fenetre
		gameWindow.configure(bg="#45458B")



# Class des lettres
class Lettre:

	def __init__(self,lettre,gameWindow,LetterButtonFont,mot):
		self.mot = mot
		self.lettre = lettre
		self.boutton = Button(gameWindow,text="".join(lettre),
			width = 3, height = 1, font = LetterButtonFont,
			 bg="#9090EE",activebackground="#A3A3FE",bd=0,
			 command = self.afficherMot)
		
	def afficherMot(self):
		self.mot += self.lettre

# Class du mot qui sera créé au fur et à mesure
class Mot:

	def __init__(self,displayLabel):
		self.lettres = ""
		self.displayLabel = displayLabel

	def ajouterLettre(self, lettre):
		self.lettres += lettre

	def afficherMot(self):
		self.displayLabel.