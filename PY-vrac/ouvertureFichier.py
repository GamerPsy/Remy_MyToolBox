#tableau =[]
#file = open("testLecture", "r")
#for lignes in file :
#	tableau.append(lignes)
#print(tableau)
#file.close()	

tableau2 =[]
file = open("testLecture", "r")
contenu = file.read()
for lignes in file :
	tableau2.append(lignes)
print(tableau2)
print("------------------------------------")	
print(contenu)
file.close()	
