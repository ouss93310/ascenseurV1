# -*- coding: utf-8 -*-

import random  #module qui va générer nos positions 
import time

def go_ascenseur (position_ascenseur, position_humain) :     
    print("l'ascenseur est à l'étage:", position_ascenseur, "et vous êtes au :", position_humain,", l'ascenseur arrive !")
    direction = position_humain-position_ascenseur
    
    if (direction>0):
        for i in range (position_ascenseur,position_humain+1): 
            print("étage", i)
            print("___")
            print("|↑|")
            print("|_|")
            time.sleep(3)


    if (direction<0):  
        for i in range (position_ascenseur,position_humain-1, (-1)): 
            print("étage", i)
            print("___")
            print("| |")
            print("|↓|")
            time.sleep(3)


    print("ouverture des portes !")
    print(" ___")
    print("| ⇶ ")        
    print("|_ _")
    time.sleep(3)
    print("fermeture des portes !")
    print(" ___")
    print("|⬱")        
    print("|_ _")
    


def disponibilite(availability): 
    print(availability)
    liste_attente = []
    new_liste = []
    if (availability): 
        go_ascenseur(random.randrange(0,10),random.randrange(0,5))
    
    while (not(availability) and len(liste_attente) < 10): 
        liste_attente.append([random.randrange(0,10),random.randrange(1,6)])

    for n in liste_attente: 
        if n in new_liste : 
         pass    
        else : 
         new_liste.append(n)
    print(new_liste)
    for [n,m] in new_liste : 
        go_ascenseur(n,m)
        

disponibilite(random.randrange(0,2))