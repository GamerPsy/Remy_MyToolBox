ligne = 10

for i in range(1, ligne+1):
	print("*"*i)


for i in range(ligne):
	if i < 3 or i==ligne-1 :
		print("*"*i)
	else :
		nb_zero = i-2
		print("*"+"0"*nb_zero+"*")