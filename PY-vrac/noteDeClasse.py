#----------------------------
#definition procedure
#----------------------------
def noteDeClasse():
    stop=True
    tableau=[]
    sommes=0
    moyenne=0
    mediane=0
    supMoyenne=0

#----------------------------    
#procedure d'entree de donnee
#----------------------------
    while stop:
        entree=input("veuillez entrer une note s'il vous plait (-1 pour arreter) : ")
        entree=int(entree)
        if entree>=0:
            tableau.append(entree)
        else:
            stop=False
#----------------------------
# on trie le tableau
#----------------------------
    tableau.sort()

#----------------------------            
#calcul de la somme
#----------------------------
    for i in tableau:
        sommes+=i

#----------------------------        
#calcul de la moyenne
#----------------------------
    if len(tableau)!=0:
        moyenne = sommes/len(tableau)

#----------------------------    
#calcul mediane
#----------------------------
    if len(tableau)%2==0:
        mediane=(tableau[(len(tableau)//2)]+tableau[(len(tableau)//2)-1])/2
    else:
        mediane=tableau[(len(tableau)//2)]

#----------------------------------------------        
#calcul nombe de notes au dessus de la moyenne
#----------------------------------------------
    for i in tableau:
        if i>moyenne:
            supMoyenne+=1

#----------------------------                            
#visualtisation des resultats
#----------------------------
    print("La moyenne est de "+str(moyenne))
    print("-------------------------------------")
    print("La mediane est de "+str(mediane))
    print("-------------------------------------")
    print("Et il y a "+str(supMoyenne)+" note(s) au dessus de la moyenne.")
noteDeClasse()