alphaLower = []
alphaUpper = []
indice = []

for ascii in range(ord('a'), ord('z') + 1):
   alphaLower.append(chr(ascii))

for ascii in range(ord('A'), ord('Z') + 1):
   alphaUpper.append(chr(ascii))


carSecret = input()
carSecret = list(carSecret)
texte = input()
texte = list(texte)


for i in range(len(carSecret)):
   if texte[i] in alphaLower :
       texteId = alphaLower.index(texte[i])
   else: texteId = alphaUpper.index(texte[i]) 
   print(texteId)
   indice[i] = texteId

   
   for i in texte:
      message = texte[i].replace(texte[i], carSecret[texteId])   
      print(message)