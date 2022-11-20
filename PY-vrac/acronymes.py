acronyme = list(input())
boucle_acro = len(acronyme)

nbLivres = int(input())
validation = 0

for livre in range(nbLivres):
   titre = input().lower().title()
   titre2 = titre.split()
   
   if (len(acronyme)) == (len(titre2)):
      for lettre in range(len(titre2)):
         if titre2[lettre][0] == acronyme[lettre]:
            validation +=1
      if validation == boucle_acro:
         print(titre)
      validation = 0
         
        