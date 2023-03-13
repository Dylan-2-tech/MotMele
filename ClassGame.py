from tkinter import *
from tkinter import ttk
import tkinter.font as font

# Fichier des classdu jeu
# Class boutton ou lettre


class Lettre:

	def __init__(self,lettre,gameWindow,LetterButtonFont):
		self.boutton = Button(gameWindow,text="".join(lettre),width = 4, height = 3, font = LetterButtonFont)
