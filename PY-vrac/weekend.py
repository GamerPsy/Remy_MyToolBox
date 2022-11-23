weekend = ["samedi", "dimanche"]
semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]

jour = input("Veuillez saisir un jour de la semaine : ")
jour=jour.lower()

if jour in weekend:
	print("\n====> Le jour saisit est dans le WEEKEND")
elif jour in semaine:
	print ("\n====>Le jour saisit est en SEMAINE")
else:
	print("\n====> Le jour saisit est INCORRECT, les jour valides sont : lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche.")