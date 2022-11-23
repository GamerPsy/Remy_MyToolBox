# Bataille

Le but de ce dojo est de déterminer quel est le joueur gagnant d'une manche de Bataille.

ex : 
- P1 joue un 3, P2 joue un 4 => l'algo doit retourner 'P2'
- P1 joue une Dame, P2 un 8 => l'algo doit retourner 'P1'
- Les deux joueurs jouent un Roi, l'algo doit retourner 'Bataille' (on ne s'occupe pas des tours suivants dans ce cas)

Entrée : 2 strings, la carte jouée par le player 1 et la carte jouée par le player 2
Les cartes (dans l'ordre de leur force, doivent être sous la forme) :

    A<2<3<4<5<6<7<8<9<10<V<D<R

> La carte la moins forte est l'As, la plus forte le Roi.
    
Sortie : Le joueur gagnant la manche, soit 'P1', soit 'P2', soit 'Bataille' si les cartes sont de valeurs égales.