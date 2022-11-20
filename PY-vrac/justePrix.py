# écrire un programme du juste prix
import random
nbAleatoire = random.randint(0,100)
limite = 5

while limite > 0 :
	essai = int(input("Quel est le juste prix selon vous ? "))
	if essai == nbAleatoire :
		print("GAGNE !")
		limite = 0
	elif essai < nbAleatoire :
		limite -=1
		print("----- C'est plus ! Il vous reste " + str(limite) + " essai(s)")
	elif essai > nbAleatoire :
		limite -=1
		print("----- C'est moins ! Il vous reste " + str(limite) + " essai(s)")		

print("Il fallait trouver " + str(nbAleatoire))
