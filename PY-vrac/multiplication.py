chiffre1=input("veuillez rentrer le premier chiffre : ")
chiffre2=input("veuillez rentrer le deuxieme chiffre : ")
chiffre1=int(chiffre1)
chiffre2=int(chiffre2)
resultat=0
for i in range(abs(chiffre2)):
    resultat+=chiffre1
if chiffre2<0:
    resultat=-resultat
print("le resultat est : "+str(resultat))