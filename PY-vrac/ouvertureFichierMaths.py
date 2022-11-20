tableau = []
file = open("DonneesMath.txt", "r")
for lignes in file :
	tableau.append(lignes)

longueur = ""
largeur = ""
for i in tableau[1] :
	if i.isnumeric():
		longueur += i

for i in tableau[2] :
	if i.isnumeric():
		largeur += i		


def aire(longueur, largeur) :
	resultat = int(longueur) * int(largeur)
	return resultat

print(aire(longueur, largeur))