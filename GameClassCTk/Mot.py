
# Class du mot
class Mot:

	def __init__(self):
		self.text = []

	def __str__(self):
		return "".join(self.text[i].lettre for i in range(len(self.text)))

	def get_mot(self):
		return "".join(self.text[i].lettre for i in range(len(self.text)))

	def clear_mot(self):
		self.text = []

	def valider_mot(self):
		for lettre in self.text:
			lettre.isClicked = False
			lettre.boutton.configure(fg_color = ("#9287C7","#5F5591"), 
			hover_color = ("#BCB3E4","#746AA4"), border_color = ("#51AF70","#337D4B"))

	def ajouter_Lettre(self, lettre):
		self.text.append(lettre)

	def mot_correct(self):
		"""Renvoie True si chaque lettre du mot suivent la même direction.

		En mathématiques, (x,y) sont les coordonnées basiques d'un graphe pour trouver un point.
		En informatique lorsqu'on veux créer une map en 2D n ne peut pas utiliser cette représentation
		des positions des objet que l'on veut placer dans la map.
		Une "MAP" en info c'est une liste de liste.
		Supposons que nous avons une map comme la suivante:

			Map = [["a","b","c","d"],
				   ["e","f","g","h"],
				   ["i","j","k","l"]]

		En graphe le point à la position (3,4) est "l" mais en informatique c'est Map[3][2].
		On soustrain 1 au deux coordonnées et on place d'abord les y puis les x.
		"""

		if len(self.text) > 1: # Si le mot a plus de une seule lettre
			if self.mot_horizontal(): # Si le mot est horizontal
				return True
			elif self.mot_vertical(): # Si le mot est vertical
				return True
			elif self.mot_diagonale_gauche_droite(): # Si le mot est en diagonale de gauche à droite
				return True
			elif self.mot_diagonale_droite_gauche(): # Si le mot est en diagonale de droite à gauche
				return True
			else: # Si le mot n'est pas bien formé
				return False
		else: # Si le mot est composé de qu'une seule lettre
			return False
	

	def mot_horizontal(self):
		# Si toutes les lettres sont positionné horizontalement

		startX = self.text[0].x # Position x pour comparer les positions avec self.text[indLetter].x
		startY = self.text[0].y # Position y pour comparer les positions avec self.text[indLetter].y
		indLetter = 1 # Indice pour comparer les position entre lettres. On commence avec la 2ème lettre car startX et startY sont les position de la première lettre
		wellFormed = True # Booléen pour entrer dans la boucle 

		while wellFormed and indLetter < len(self.text): # Tant que le mot semble être horizontale et qu'on a pas fini de le parcourir
			# ENORME condition pour savoir si les lettres se suivent horizontalement
			wellFormed = (self.text[indLetter].x == startX and self.text[indLetter].y == startY+1) or (self.text[indLetter].x == startX and self.text[indLetter].y == startY-1)
			startY = self.text[indLetter].y # On actualise la position en y avec celle de la lettre comparé au tour d'avant 
			indLetter += 1 # On augmente pour comparer avec la lettre suivante

		if wellFormed: # Si le mot est bien formé
			return True # On retourne True
		else: # Sinon
			return False # On retourne False

	def mot_vertical(self):
		# Si toutes les lettres sont positionné verticalement

		startX = self.text[0].x # Position x pour comparer les positions avec self.text[indLetter].x
		startY = self.text[0].y # Position y pour comparer les positions avec self.text[indLetter].y
		indLetter = 1 # Indice pour comparer les position entre lettres. On commence avec la 2ème lettre car startX et startY sont les position de la première lettre
		wellFormed = True # Booléen pour entrer dans la boucle 

		while wellFormed and indLetter < len(self.text): # Tant que le mot semble être verical et qu'on a pas fini de le parcourir
			# ENORME condition pour savoir si les lettres se suivent verticalement
			wellFormed = (self.text[indLetter].x == startX+1 and self.text[indLetter].y == startY) or (self.text[indLetter].x == startX-1 and self.text[indLetter].y == startY)
			startX = self.text[indLetter].x # On actualise la position en x avec celle de la lettre comparé au tour d'avant 
			indLetter += 1 # On augmente pour comparer avec la lettre suivante

		if wellFormed: # Si le mot est bien formé
			return True # On retourne True
		else: # Sinon
			return False # On retourne False

	def mot_diagonale_gauche_droite(self):
		# Si toutes les lettres sont positionnées en diagonale de à gauche à droite

		startX = self.text[0].x # Position x pour comparer les positions avec self.text[indLetter].x
		startY = self.text[0].y # Position y pour comparer les positions avec self.text[indLetter].y
		indLetter = 1 # Indice pour comparer les position entre lettres. On commence avec la 2ème lettre car startX et startY sont les position de la première lettre
		wellFormed = True # Booléen pour entrer dans la boucle 

		while wellFormed and indLetter < len(self.text):
			# ENORME condition pour savoir si les lettres se suivent en diagonale de à gauche à droite
			wellFormed = (self.text[indLetter].x == startX+1 and self.text[indLetter].y == startY+1) or (self.text[indLetter].x == startX-1 and self.text[indLetter].y == startY-1)
			startX = self.text[indLetter].x # On actualise la position en x avec celle de la lettre comparé au tour d'avant
			startY = self.text[indLetter].y # On actualise la position en y avec celle de la lettre comparé au tour d'avant
			indLetter += 1 # On augmente pour comparer avec la lettre suivante

		if wellFormed: # Si le mot est bien formé
			return True # On retourne True
		else: # Sinon
			return False # On retourne False

	def mot_diagonale_droite_gauche(self):
		# Si toutes les lettres sont positionnées en diagonale de droite à gauche

		startX = self.text[0].x # Position x pour comparer les positions avec self.text[indLetter].x
		startY = self.text[0].y # Position y pour comparer les positions avec self.text[indLetter].y
		indLetter = 1 # Indice pour comparer les position entre lettres. On commence avec la 2ème lettre car startX et startY sont les position de la première lettre
		wellFormed = True # Booléen pour entrer dans la boucle 

		while wellFormed and indLetter < len(self.text):
			# ENORME condition pour savoir si les lettres se suivent en diagonale de droite à gauche
			wellFormed = (self.text[indLetter].x == startX+1 and self.text[indLetter].y == startY-1) or (self.text[indLetter].x == startX-1 and self.text[indLetter].y == startY+1)
			startX = self.text[indLetter].x # On actualise la position en x avec celle de la lettre comparé au tour d'avant
			startY = self.text[indLetter].y # On actualise la position en y avec celle de la lettre comparé au tour d'avant
			indLetter += 1 # On augmente pour comparer avec la lettre suivante

		if wellFormed: # Si le mot est bien formé
			return True # On retourne True
		else: # Sinon
			return False # On retourne False
