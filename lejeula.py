from tkinter import *
from tkinter import ttk
import tkinter.font as font
from ClassGame import Lettre

gameMap = [ ["A","B","G","N","I","Z"],
			["B","H","Y","A","W","Q"],
			["H","R","D","T","P","O"],
			["L","J","G","Z","I","M"],
			["E","X","B","N","K","M"],
			["X","T","S","L","G","Y"],
			]

gameWindow = Tk()
gameWindow.title("lejeula")
gameWindow.geometry("800x800")


#Leave button
leaveBtn = Button(gameWindow,text="Quitter",bg = "red",fg = "white",command=gameWindow.destroy)
leaveBtn.place(x=700,y=600)

# Buttons fonts
LetterButtonFont = font.Font(size=20)
LeaveButtonFont = font.Font(size=10)


# boutton
#generating the map

posy = 0
for x in range(len(gameMap[0])):
	posx = 0
	posy += 115
	for y in range(len(gameMap)):
		lettre = Lettre(gameMap[x][y],gameWindow,LetterButtonFont)
		lettre.boutton.place(x=posx, y=posy)
		posx+=100

gameWindow.mainloop()

