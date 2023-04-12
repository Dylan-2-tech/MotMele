"""
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
import random
import string
import glob
import sys
"""

#### Importation des classes du jeu ####
from GameClassCTk.Menu import Menu
from GameClassCTk.Creation import Creation
from GameClassCTk.Jeu import Jeu
from GameClassCTk.Mot import Mot

#### Lancement du jeu ####
Jeu = Jeu("Grille2")

Jeu.mainloop()