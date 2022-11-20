entree = input()
entree = entree.upper()


# Dictionnaire des caractères contenus dans l'entrée avec leur occurence
compteur={}
for car in entree:
    compteur[car]=compteur.get(car,0)+1
del compteur[" "]
maximum = max(compteur, key=compteur.get)
print(maximum) 
