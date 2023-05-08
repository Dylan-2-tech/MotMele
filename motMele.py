
#### Importation des classes du jeu ####
from GameClassCTk.Creation import Creation
from GameClassCTk.Menu import Menu
from GameClassCTk.Menu import MessageBox
from GameClassCTk.Jeu import Jeu


#### Lancement du jeu ####

Jeu = Menu()


"""
for i in range(20):
	with open(f"mot/grille{i}.txt", "w") as f:
		f.writelines(str(i))
	with open(f"grille/grille{i}.txt", "w") as f:
		f.writelines(str(i))"""