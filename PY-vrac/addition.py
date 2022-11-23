chiffre1=input("veuillez rentrer le premier chiffre : ")
chiffre2=input("veuillez rentrer le deuxieme chiffre : ")
chiffre1=int(chiffre1)
chiffre2=int(chiffre2)
for i in range(chiffre2):
    chiffre1+=1
print("le resultat est : "+str(chiffre1))