weekend=["samedi", "dimanche", "Samedi", "Dimanche", "saturday", "sunday", "Saturday", "Sunday"]
jour=input("Veuillez rentrer le jour de la semaine : ")
if jour in weekend:
    print("Vous etes bien dans le weekend")
else :
    print("Vous etes en semaine")