def pgcd(x,y):
    if x == 0:
        return y
    elif y == 0:
        return x
    elif x > y:
        return pgcd(x-y, y)
    else:
        return pgcd(x, y-x)


resultat = pgcd(50,30)
print("Le PGCD est "+str(resultat))