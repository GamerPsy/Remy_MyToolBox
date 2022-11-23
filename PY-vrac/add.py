operateurs = ["+", "-", "*"]
nb1 = int(input("Renseigner un chiffre : "))
nb2 = int(input("Renseigner un chiffre : "))
operateur = input("Choisir l'opérateur parmi +,-,* :")

compteur=1
resultat=0 #nécessaire pour la multiplication
while (compteur <=nb2 and operateur in operateurs): 
	if operateur == "+":
		nb1+=1
	elif operateur == "-":
		nb1-=1
	elif operateur == "*":
		resultat+=nb1
	compteur+=1
if (operateur == "+" or operateur == "-" ) :
	print(nb1)
elif operateur == "*" :
	print(resultat)
else : 
	print("opérateur non valide : à recommencer !")
