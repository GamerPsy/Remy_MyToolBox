result1 = [0]
result3 = 0
try:
   nbLignes = int(input())
   for loop in range(nbLignes):

      saisie = input()

      if len(saisie) == 1 :
         saisie = [int(i) for i in saisie]
         result1[0] = result1[0] + saisie[0]
         print(result1[0])
      else:
         saisie = saisie.split()
         result2 = [int(i) for i in saisie]
         result2 = sum(result2)
         result3 = result3 + result2        
except: pass

somme = result1[0] + result3
somme = round(float(somme))
print(somme)