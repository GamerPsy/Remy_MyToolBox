valide=True
while valide:
    heure=input("veuillez saisir une heure au format HH:MM s'il vous plait : ")
    if int(heure[0])==0 or int(heure[0])==1:
        if int(heure[1])>=0 and int(heure[1])<=9 and heure[2]==":":
            if int(heure[3])>=0 and int(heure[3])<=6:
                if int(heure[4])>=0 and int(heure[4])<=9:
                    valide=False
    if int(heure[0])==2:
        if int(heure[1])>=0 and int(heure[1])<=3 and heure[2]==":":
            if int(heure[3])>=0 and int(heure[3])<=5:
                if int(heure[4])>=0 and int(heure[4])<=9:
                    valide=False                

if int(heure[4])!=9:
    heure=heure[0:4]+str(int(heure[4])+1)
elif int(heure[3])!=5:
    heure=heure[0:3]+str(int(heure[3])+1)+"0"
elif int(heure[0])==2 and int(heure[1])!=3:
    heure=heure[0]+str(int(heure[1])+1)+":00"
elif (int(heure[0])==1 or int(heure[0])==0) and int(heure[1])!=9:
    heure=heure[0]+str(int(heure[1])+1)+":00"
elif int(heure[0])!=2:
    heure=str(int(heure[0])+1)+"0:00"
else:
    heure="00:00"
print(heure)