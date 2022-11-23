import random

def justePrix(essai, valeur):
	alea = random.randint(0,valeur)
	saisie = True
	
	for i in range(essai+1) :
		while saisie :
			entree = -1
			try :
				entree = int(input("Veuillez saisir un chiffre entre 0 et "+str(valeur)+" : "))
			except ValueError :
				print("Vous n'avez pas rentré un chiffre entier")
			if	(entree > valeur or entree < 0):
				print("la valeur entrée est incorrecte")
			else:
				saisie = False
		
		if entree > alea :
			print("\n---------------------------------------\n")
			print("Le juste prix est plus BAS !!\n\nIl vous reste "+str(essai-i)+" essais !")
			print("\n---------------------------------------\n")
			saisie = True
		elif entree<alea :
			print("\n---------------------------------------\n")
			print("Le juste prix est plus HAUT !!\n\nIl vous reste "+str(essai-i)+" essais !")
			print("\n---------------------------------------\n")
			saisie = True
		elif entree==alea :
			print("\n---------------------------------------\n")
			print("Bravo, vous avez gagné en "+str(i+1)+" essai(s)")
			break
		if i==essai :
			print("\n---------------------------------------\n")
			print("Dommage vous n'avez plus d'essais")
			

saisie_essai = True
essai = -1
saisie_max = True
max = -1

while saisie_essai :
	try :
		essai = int (input("Veuillez renseigner un nombre d'essai : "))
	except ValueError :
		print("Vous n'avez pas renseigné un chiffre !")
	if essai < 3:
		print ("Renseignez un chiffre supérieur à 3 !")
	else :
		saisie_essai = False

while saisie_max :
	try :
		max = int (input("Veullez renseigner une borne maximum : "))
	except ValueError :
		print ("Vous n'avez pas renseigné un chiffre !")
	if max <10 :
		print("renseignez un chiffre supérieur à 10 !")
	else :
		saisie_max = False
		
justePrix(essai, max)