#écrire un script qui demande une heure au format HH:MM
demandeHeure = input("Veuillez saisir une heure au format HH:MM : ")
traitementHeure = demandeHeure.split(":")
heures = traitementHeure[0]
minutes = int(traitementHeure[1]) + 1
print(str(heures) + ":" + str(minutes))

