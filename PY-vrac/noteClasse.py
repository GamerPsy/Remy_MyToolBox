#Algo permettant de saisir note de classe
# s'il veut s'arrêter il tape -1
# Le programme renvoie la moyenne, la médiane, le nombre de note au dessus de la moyenne
import statistics

notes = []
nbEleves = 0
script = True
supMoyenne = 0

while script :
	notesClasses = int(input("Veuillez entrer une note : "))
	if notesClasses == -1 :
		script = False
		print("Fin de saisie, merci.")
	else :
		nbEleves += 1
		notes.append(notesClasses)

notes.sort()
moyenne = sum(notes)/nbEleves
mediane = statistics.median(notes)

for i in range(nbEleves) :
	if notes[i] > moyenne :
		supMoyenne +=1

print("La moyenne est de : " + str(moyenne) + "/20")
print("La note médiane est de : " + str(mediane) + "/20")
print("Il y a " + str(supMoyenne) + " élèves qui sont au-dessus de la moyenne dans cette classe de " + str(nbEleves) + " élèves.")
