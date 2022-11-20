#Exemple de boucle avec variable de stockage, ici totalBonbons et numTir sert pour compter le nombre de tour.
#BASIQUE#

totalBonbons = 0
numTir = 1
for loop in range(50):
   totalBonbons = totalBonbons + numTir
   print(totalBonbons)
   numTir = numTir + 1


#POUR PRINT UN INTERVALLE DE VALEUR PAR LIGNE
#Étant données deux températures entières tempMin et tempMax, votre programme doit afficher toutes les températures comprises entre les deux, bornes incluses.

tempMin = int(input())
tempMax = int(input())
tour = tempMax - tempMin
print(tempMin)
for loop in range(tour):
   tempMin = tempMin + 1
   print(tempMin)


