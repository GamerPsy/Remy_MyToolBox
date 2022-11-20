# l'indentation 
une TAB correspond à ... 


#Print sans retour à la ligne, c'est le end = ""  qui fait qu'il n'y a pas d'espace, si on en veut un end = " "
for loop in range(30):
   print("a_", end = "")


#Sauter une ligne
print()
ou alors avec une boucle qui print quelque chose sans avoir de end = ""


#faire un commentaire, on utilise soit # soit """ qu'on referme """
(En réalité, il ne s'agit pas d'un commentaire mais d'un texte du programme s'étendant sur plusieurs lignes. Sans instruction pour l'utiliser, il est cependant ignoré à l'exécution.)


#Règles pour les variables, pour les nommer
L'identifiant se constitue de caractères collés (pas d'espace), Les caractères autorisés sont essentiellement : 
les lettres majuscules et minuscules naturelles : abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ;
les chiffres 0123456789 ;
le caractère « _ » (appelé « sous-tiret »).
Le premier caractère du nom d'une variable ne peut pas être un chiffre ; le nom 1erNombre est donc invalide.
Les mots-clés du langage ne peuvent être utilisés pour nommer des variables. En Python, c'est par exemple le cas du mot for.
Dans le cas du langage Python, les accents sont acceptés dans les identifiants.
Vous devez profiter de cette flexibilité pour choisir des noms qui aideront à comprendre votre programme. Nous vous en reparlerons dans un prochain cours.


#Règle de modification de variable :
variable <- valeur
signifie que valeur devient le nouveau contenu de variable, on dit qu'on affecte la valeur à la variable.


#
