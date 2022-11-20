#Demande entrée nombre de déplacements et création du tableau des déplacements
nbDep = int(input())
Depl = [0] * nbDep

#Boucle qui va remplir au fur et à mesure des entrées le tableau des déplacements en modifiant directement pour le retour
for num in range(nbDep):
   Depl[num] = int(input()) 
   if Depl[num] == 1: 
      Depl[num] == 2 
   elif Depl[num] == 2: 
      Depl[num] == 1
   elif Depl[num] == 4:
      Depl[num] == 5
   elif Depl[num] == 5:
      Depl[num] == 4

#Boucle pour lecture du tableau de départ modifié mais dans le sens inverse soit de la fin vers le début
for num in Depl[::-1]:
   print(num)