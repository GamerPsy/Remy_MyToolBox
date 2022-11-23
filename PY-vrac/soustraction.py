chiffre1=input("veuillez rentrer le premier chiffre : ")
chiffre2=input("veuillez rentrer le deuxieme chiffre : ")
chiffre1=int(chiffre1)
chiffre2=int(chiffre2)
if chiffre2>=0:
    for i in range(chiffre2):
        chiffre1-=1
    print("le resultat est : "+str(chiffre1))
else:
    chiffre2=-chiffre2
    for i in range(chiffre2):
        chiffre1+=1
    print("le resultat est : "+str(chiffre1))