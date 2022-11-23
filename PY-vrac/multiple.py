chiffre1 = int( input ("Veuillez renseigner le chiffre n°1 : "))
chiffre2 = int( input ("Veuillez renseigner le chiffre n°2 : "))

if chiffre1>100 and chiffre2<37:
	print ("\n====> les conditions de l'exercice 1 sont respectées!!")
else:
	print ("\n====> les conditions de l'exercice 1 ne sont pas respectées !!")

print("--------------------------------------------------------")	

if chiffre1>100 or chiffre2<37:
	print ("\n====> les conditions de l'exercice 2 sont respectées!!")
else:
	print ("\n====> les conditions de l'exercice 1 ne sont pas respectées !!")