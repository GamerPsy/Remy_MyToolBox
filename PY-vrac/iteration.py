boom = 1
compteurBoom = 50
while boom <= 50 :
		boom += 1
		compteurBoom -= 1
		if compteurBoom <= 10 :
			print("Le python c'est chouette ! " + str(compteurBoom) + " avant explosion")
		else :
			print("Le python c'est chouette ! ")
		if compteurBoom == 0 :
			print("BOOOOOOOOOOOOOOOOOOOOOOOM")	