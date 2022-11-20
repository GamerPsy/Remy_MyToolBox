import collections
texteDepart = input()
texteLettres = []
denominateur = len(texteLettres)
alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]


#Création tableau avec que les lettres
for i in range(len(texteDepart)):
	if texteDepart[i].isalpha():
		texteDepart[i] = texteDepart[i].lower()
		texteLettres.append(texteDepart[i])


#occurence
compteurOccurence={}
for car in texteLettres:
    compteurOccurence[car]=compteurOccurence.get(car,0)+1

#on ordonne le dictionnaire grace à OrderedDict de collections
compteurOccurence = collections.OrderedDict(sorted(compteurOccurence.items()))
print(compteurOccurence)




"""
Pour chacune des lettres de l’alphabet, il faut afficher, sur une ligne, sa fréquence d’apparition dans le texte définie comme le nombre de fois où la lettre est présente, divisé par le nombre total de lettres du texte (et pas le nombre total de caractères).
"""
