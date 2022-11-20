#Traduire le code génétique suivant à l'aide d'un dictionnaire
#sachant que UUU = F UUC = F UUA = L UUG = L UCU = S
from textwrap import wrap

ARNm = "UUUUUAUUGUUUUCUUUU"
dictionnaire = {"UUU" : "F", "UUC" : "F", "UUA" : "L", "UUG" : "L", "UCU" : "S"}
liste = wrap(ARNm, 3)
reponse = ""

for i in range(len(liste)) :
	reponse += dictionnaire[liste[i]]
print(reponse)	
