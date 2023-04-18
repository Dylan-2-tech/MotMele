
#### Importation des classes du jeu ####
from GameClassCTk.Creation import Creation
from GameClassCTk.Menu import Menu
from GameClassCTk.Jeu import Jeu


#### Lancement du jeu ####
Jeu = Creation()

"""
from customtkinter import CTkRadioButton
import customtkinter
from customtkinter import CTkFont
from customtkinter import CTk
from customtkinter import IntVar

fenetre = CTk()
fenetre.geometry("100x100+400+400")


def des_hard():
	print(var.get())

def des_eazy():
	print(var.get())

var = IntVar()

hard = CTkRadioButton(fenetre, text = "difficile", command = des_hard, font = CTkFont(size = 20),
	hover_color = "#C22955", border_color = "#C22955", variable = var, value = 1)
eazy = CTkRadioButton(fenetre, text = "facile", command = des_eazy, font = CTkFont(size = 20),
	)

hard.grid()
eazy.grid()

fenetre.mainloop()


from customtkinter import CTkRadioButton
import customtkinter
from customtkinter import CTkFont
from customtkinter import CTk
from customtkinter import CTkLabel
from customtkinter import IntVar


def sel():
	selection = var.get()
	if selection == 1:
		print("wtf")
	else:
		print("mdf")
	

root = CTk()
var = IntVar()
R1 = CTkRadioButton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.grid()

R2 = CTkRadioButton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.grid()

R3 = CTkRadioButton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.grid()

label = CTkLabel(root)
label.grid()
root.mainloop()
"""