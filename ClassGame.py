from tkinter import *
from tkinter import ttk
import tkinter.font as font

# Fichier des classdu jeu
# Class boutton ou lettre


class Lettre:

	def __init__(self,lettre,gameWindow,LetterButtonFont):
		self.lettre = lettre
		self.boutton = Button(gameWindow,text="".join(lettre),
			width = 3, height = 1, font = LetterButtonFont,
			 bg="#9090EE",activebackground="#A3A3FE",bd=0,
			 command = self.afficher)
		
	def afficher(self):
		print(self.lettre)



