arnm = "UUUUUAUUGUUUUCUUUU"
dico = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S"}
mot = ""
for i in range(0, len(arnm), 3) :
	triplet = arnm[i:i+3]
	mot += dico[triplet]
print(mot)