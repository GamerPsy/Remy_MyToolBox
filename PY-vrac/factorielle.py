def factorielle(x) :
	if x==1 :
		return 1
	else:
		return x*factorielle(x-1)

resultat = factorielle(5)

print(resultat)