# Créer fonction avec paramètres : chaine de caractère et caractère
# Purge de la chaine de caractère précisée
def purge(entree, caractere, nombre) :
	retour = ""
	compteur = 0
	for i in entree :
		if i == caractere:
			compteur +=1
		if i != caractere or compteur > nombre:
			retour += i
	return retour		
reponse = purge("Je n'aime pas les haricots !", "a", 1)
print(reponse)
