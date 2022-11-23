#definition procedure
def purge(chaine, charactere, nombre):
    resultat=""
    compteur=0
    for i in chaine:
        if i==charactere:
            compteur+=1
        if i!=charactere or compteur>nombre:
            resultat+=i
    return resultat
#purge des "o"
purgeO=purge("Bonjour","o",1) 
print(purgeO+"\n\n")       

#purge des espaces
purgeEspace=purge("J'ai horreur des espaces !", " ",2)    
print(purgeEspace)