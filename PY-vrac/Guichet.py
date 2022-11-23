weekend = ["samedi", "dimanche"]
semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
heure = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

saisie_heure = True
saisie_jour =  True

matin = False

while saisie_heure :
	heure_entree=-1
	try :
		heure_entree = int(input("Veuillez saisir une heure : "))
	except ValueError:
		print("vous n'avez pas saisie de chiffre !")
	if heure_entree not in heure :
		print("L'heure entrée est invalide, les valeurs valide vont de 0 à 23")
	else : 
		saisie_heure = False

if heure_entree > 17 or heure_entree == 13 or heure_entree == 14 or heure_entree < 8 :
	print ("Le guichet est fermé")
else :
	if heure_entree < 13 :
		matin = True
	while saisie_jour :
		jour_entree = input("Veuillez renseigner un jour : ")
		jour_entree = jour_entree.lower()
		if jour_entree in semaine or jour_entree == weekend[0] :
			saisie_jour = False
		elif jour_entree == weekend[1] :
			print("Le guichet est fermé")
			saisie_jour = False
		else : 
			print("Vous n'avez pas saisie de jour valide (Lundi, Mardi, Mercredi, Jeudi, Vendredi, Samedi, Dimanche")
	if jour_entree == weekend[0] and matin == False : 
		print("Le guichet est fermé !")
	elif jour_entree != weekend[1] : 
		print("Le guichet est ouvert")
		