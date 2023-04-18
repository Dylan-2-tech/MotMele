
"""
import string

def ascii_in(mot):

	correct = True
	indc = 0

	while correct and indc < len(mot):
		correct = mot[indc] in string.ascii_lowercase or "\n" in mot[indc]
		indc += 1

	return correct


# nettoyage des mots
with open('../mot/liste_francais.txt', "r+", encoding = "latin-1") as f:
	words = [word.lower() for word in f if len(word) < 11 and len(word) > 5] # Entre 4 et 9 pck \n vaut 1 
	words = [word for word in words if ascii_in(word)]
f.close()


with open('../mot/liste_mots.txt', 'w') as f:
	f.writelines(words)
"""


grille = [["" for i in range(9)] for i in range(9)]

def affichage_grille(g):

	for listeLettre in grille:
		print(listeLettre)

affichage_grille(grille)
