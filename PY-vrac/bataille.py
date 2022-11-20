joueur1=input()
joueur2=input()
egalite=0
minimum=min(len(joueur1),len(joueur2))
 
if joueur1==joueur2:
   egalite = egalite +1
   print("=")

for i in range(minimum):
   if joueur1[i]==joueur2[i] : 
      egalite+=1


   elif joueur1[i]>joueur2[i] :
      print("2")
      break

   elif joueur2[i]>joueur1[i]:
      print("1")
      break


   elif len(joueur1) > min:
      print("1")
      break
   elif len(joueur2) > min:
      print("2")
      break


print(egalite)
#Il m'en valide 11 sur 14
#parce que je n'arrive pas à entrer le cas où l'un à moins de carte que l'autre