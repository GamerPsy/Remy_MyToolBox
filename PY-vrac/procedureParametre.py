def procedurePython(repetition, langage):
    for i in range(repetition):
        if langage=="espace":
            print("-----espace-----")
        else:
            print("Le "+langage+" c'est chouette. compteur : "+str(i))
procedurePython(2, "Python")
procedurePython(1, "espace")
procedurePython(3, "Java")
procedurePython(1, "espace")
procedurePython(4, "Ruby")