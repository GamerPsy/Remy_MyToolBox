#Coder la permutation circulaire droite de 4 entiers x, y, z, t
print("Exercice inversion de valeur :")
tableau = [1, 2, 3, 4]
inversion = tableau[3]
print(tableau)
del tableau[3]
tableau.insert(0,inversion)
print(tableau)


#Ecrire un algorithme permettant de donner la valeur absolue d'un chiffre
print("Exercice valeur absolue :")
chiffre = int(input("Merci de donner un chiffre : "))
if chiffre < 0 :
	chiffre = chiffre * -1
	print(chiffre)
else :
	print(chiffre)

#Ecrire un script permettant de déterminer l'état du guichet (ouvert, fermé)
# en fonction du jour semaine => ouvert et Weekend => fermé
# de l'heure 8-13h et 14-17 ouvert et autres horaires fermé
#Même chose mais ouvert le samedi matin
semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
jourPassage = input("Quel jour ? ")
heurePassage = int(input("Quelle heure ? "))

if (jourPassage == semaine[5] and heurePassage < 8 and heurePassage > 13) or jourPassage == semaine[6] :
	print("Désolé le magasin est Fermé ce jour là")
elif (heurePassage >= 8 and heurePassage <= 13) or (heurePassage >= 14 and heurePassage <= 17) :
	print("Le magasin est ouvert")
elif jourPassage == semaine[5] and (heurePassage >= 8 and heurePassage <= 13) :
	print("Le magasin est ouvert ce samedi matin !")
else :
	print("Le magasin est Fermé")

#Ecrire un code permet de créer une pyramide à n ligne
print("Exercice pyramide avec que des *")
pyramide = int(input("Combien de lignes ? "))
dessin =""
for i in range(pyramide) :
	dessin += "*"
	print(dessin)

#Puis tel que 
#*
#**
#*0*
#*00*
print("Pyramide avec des 0 à l'intérieur")
pyramide = int(input("Combien de lignes ? "))
etoiles = "*"
zeros = "0"
compteur = 0
while compteur < pyramide :
	if compteur == 1 :
		etoiles += "*"
	else :
		etoiles = "*"
	print(etoiles)	
	compteur += 1
	
		

#Programmer les opération de calcul élémentaire (+ - * ) sans les opérateurs, 
#seul l'incrémentation est autorisée.