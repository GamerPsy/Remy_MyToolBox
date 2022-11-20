minuscules = "abcdefghijklmnopqrstuvwxyz"
majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

crypte = ""

nbPages = int(input())
numpage =1
cle = 0

for loop in range(nbPages-1):
   texte = input()
   numpage +=1

   if numpage%2 == 0:
      cle = numpage * -3
   elif numpage %2 != 0:
      cle = 5*numpage 

   for lettre in texte:
      if lettre in minuscules:
         ind = minuscules.find(lettre)
         nouvelindex = ind + cle
         
         while nouvelindex>25 or nouvelindex<-25:
            if nouvelindex>25:
               nouvelindex -=26
            elif nouvelindex<-25:
               nouvelindex +=26
         crypte += minuscules[nouvelindex]

      elif lettre in majuscules:        
         ind = majuscules.find(lettre)
         nouvelindex = ind + cle
         
         while nouvelindex>25 or nouvelindex<-25:
            if nouvelindex>25:
               nouvelindex -=26
            elif nouvelindex<-25:
               nouvelindex +=26
            
         crypte += majuscules[nouvelindex]
         
      else :
         crypte += lettre

   print(crypte)
   crypte =""