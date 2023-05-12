
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


def affichage_grille(g):
	for listeLettre in grille:
		print(listeLettre)

grille = [["" for i in range(9)] for i in range(9)]
liste_mot = ["manger","siffler","caillou"]

#grille[3][7] = 'T'
affichage_grille(grille)

#### Fonctions qui placent le mot dans la grille de 4 manière différentes ####

# Fonction qui place un mot donner à la verticale
def search_vert(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if y < len(grille) and (grille[y][x] == "" or grille[y][x] == mot[indC]):
			liste_positions.append((x,y))
			indC += 1
			y += 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True
# Fonction qui place un mot donner à la verticale en inversant le mot
def search_vert_inv(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if y >= 0 and (grille[y][x] == "" or grille[y][x] == mot[indC]):
			liste_positions.append((x,y))
			indC += 1
			y -= 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True

# Fonction qui place un mot donner à l'horizontale
def search_hori(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if x < len(grille[0]) and (grille[y][x] == "" or grille[y][x] == mot[indC]):
			liste_positions.append((x,y))
			indC += 1
			x += 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True
# Fonction qui place un mot donner à l'horizontale en inversant le mot
def search_hori_inv(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if x >= 0 and (grille[y][x] == "" or grille[y][x] == mot[indC]):
			liste_positions.append((x,y))
			indC += 1
			x -= 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True

# Fonction qui place un mot donner en diagonale de gauche à droite
def search_diag_gd(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if x < len(grille[0]) and y < len(grille) and (grille[y][x] == "" or grille[y][x] == mot[indC]):
			liste_positions.append((x,y))
			indC += 1
			y += 1
			x += 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True
# Fonction qui place un mot donner en diagonale de gauche à droite en inversant le mot
def search_diag_gd_inv(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if x >= 0 and y >= 0 and (grille[y][x] == "" or grille[y][x] == mot[indC]):
			liste_positions.append((x,y))
			indC += 1
			y -= 1
			x -= 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True

# Fonction qui place un mot donner en diagonale de droite à gauche
def search_diag_dg(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if x >= 0 and y < len(grille) and (grille[y][x] == "" or grille[y][x] == mot[indC]):
			liste_positions.append((x,y))
			indC += 1
			y += 1
			x -= 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True
# Fonction qui place un mot donner en diagonale de droite à gauche en inversant le mot
def search_diag_dg_inv(mot, x, y):
	liste_positions = []
	indC = 0

	while indC < len(mot):
		if x < len(grille[0]) and y >= 0 and (grille[y][x] == "" or grille[y][x] == mot[indC]):
			liste_positions.append((x,y))
			indC += 1
			y -= 1
			x += 1
		else:
			print("Le mot dépasse les limites de la grille")
			return False
	
	placer_mot(mot, liste_positions)
	return True

# Fonction qui retourne sous forme de liste les positions de la lettre dans le mot entré en paramètres
def search_lettre_ind(mot, lettre):

	positions = []

	for i in range(len(mot)):
		if mot[i] == lettre:
			positions.append(i)

	return positions


def search_vert_croise(mot, positions):

	for l, p in positions.items():
		spaceOver = p[1]
		spaceBelow = len(grille)-(p[1]+1)

		indice = search_lettre_ind(mot, l)

		lenOver = len(mot)-(len(mot)-indice[0])
		lenBelow = (len(mot)-indice[0])-1

		print(f"Espace libre au dessus puis en dessous de {l}: ({spaceOver},{spaceBelow})")
		print(f"Le mot requiert une place minimum de ({lenOver},{lenBelow}) pour être verticale")

		# Condition pour pouvoir placer le mot à la verticale dans l'ordre
		if lenOver <= spaceOver and lenBelow <= spaceBelow:
			search_vert(mot, p[0], spaceOver-lenOver)
		
		#print(l, search_lettre_ind(mot, l), p)



# Fonction qui recherche un endroit ou croisé le mot
def search_croise(mot):

	positions = {}

	# Parcours de la grille
	for y in range(len(grille)):
		for x in range(len(grille[0])):
			# Si la lettre est dans le mot à placé
			if grille[y][x] in mot and grille[y][x] != "":
				positions[grille[y][x]] = (x,y)

	print(positions)

	search_vert_croise(mot, positions)
	

# Fonction pour placer les lettres du mot au positions voulu
def placer_mot(mot, liste_positions):
	# On parcours les position et on place chaque lettre du mot
	for i in range(len(liste_positions)):
		# Récupération des positions
		x = liste_positions[i][0]
		y = liste_positions[i][1]

		# Affectation des lettres du mot dans les cases vides de la grille
		grille[y][x] = mot[i]

print(search_diag_dg("mamger", 6, 1))
search_croise("pagaille")
search_vert("rie", 1, 6)
#search_croise("rie")
#print(search_hori_inv("voir", 3, 8))
#print(search_vert_inv("paille", 4, 5))
#print(search_diag_dg("grange", 8, 1))
affichage_grille(grille)

'''
REVERSE D'UNE CHAINE DE CARACTERE: [::-1]
'''