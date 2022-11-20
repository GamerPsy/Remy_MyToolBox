# écrire algoritme de la fonction factorielle
factorielle = int(input("Veuillez renseigner le chiffre pour le calcul de la fonction factorielle : "))
reponse = 1

for i in range(factorielle) :
	multiplier = factorielle - i
	reponse *= multiplier

print("Le résultat de la fonction factorielle de " + str(factorielle) + " est " + str(reponse))
