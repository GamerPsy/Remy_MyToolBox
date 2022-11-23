# on definit les jours valides
tableau = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
# on demande de renseigner jour et heure
jour=input("Veuillez saisir un jour : ")
heure=input("Veuillez saisir une heure : ")
heure=int(heure)
# on verifie qu'on ne demande pas le samedi apres midi
if jour=="samedi" or jour=="Samedi":
    if heure<8 or heure>13:
        jour=""
# on verifie qu'on est dans la bonne plage horaire
booleen = False
if (heure>8 and heure<13) or (heure>14 and heure<17):
    booleen=True
# on repond en fonction de la combinaison jour/heure
if jour in tableau and booleen:
    print("Le guichet est bien ouvert")
else:
    print("Le guichet est ferme")