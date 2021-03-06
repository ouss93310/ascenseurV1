
# -*- coding: utf-8 -*-

import random  #module qui va générer nos positions 
import time #gérer le temps

"""définition de ma fonction qui va gérer les position 
et définir le sens de direction, soit monter, soit descendre"""

def go_ascenseur (position_ascenseur, position_humain) :     
    #j'affiche les deux positions
    print("l'ascenseur est à l'étage:", position_ascenseur, 
          "et vous êtes au :", position_humain,", l'ascenseur arrive !")
    #direction va me servir à définir le sens du mouvement
    direction = position_humain-position_ascenseur
    
    #si poisitif je monte
    # j'ai mis position_humain+1 car python débute de (min) s'arrête à (max-1)
    if (direction>0):
        for i in range (position_ascenseur,position_humain+1): 
            print("étage", i)
            print("___")
            print("|↑|")
            print("|_|")
            time.sleep(3) # une pause de 3 sec 

    #si négatif je descends 
    # dans ce cas là on ajoute pas un (car direction négatif) mais soustrait 1
    # 3 eme arguement ici (-1) veut dire saut par -1 (ordre décroissant)
    if (direction<0):  
        for i in range (position_ascenseur,position_humain-1, (-1)): 
            print("étage", i)
            print("___")
            print("| |")
            print("|↓|")
            time.sleep(3) #pause de 3 sec

    print("ouverture des portes !")
    print(" ___")
    print("| ⇶ ")        
    print("|_ _")
    time.sleep(3) #pause de 3sec
    print("fermeture des portes !")
    print(" ___")
    print("|⬱")        
    print("|_ _")
    time.sleep(3) #pause de 3 sec
    
#fonction principale qui va tout gérer avec ma fonction ci-dessus
    
def disponibilite(availability): 
    #ici availability sera un boolean qu'on va fournir à la fonction après 
    print(availability)
    #deux liste vides 
    liste_attente = []
    new_liste = []
    #si ascenseur dispo
    if (availability): 
        print("Ascenseur disponible")
        #ici on demande à la machine de choisir 2 positions aléatoires [0-9] compirs
        go_ascenseur(random.randrange(0,10),random.randrange(0,10))
    else: 
        print("Ascenseur pas disponible, veuillez attendre votre tour")
       #tant que ascenseur pas disponible 
       # len(liste_attente) <5 pour avoir une liste de mois de 5 items
    while (not(availability) and len(liste_attente) < 5): 
        #on récupère la liste qui sera ensuite stockée dans liste_attente
        #liste_attente=[nouvelle_position_ascenseur, position_personne en attente]
        liste_attente.append([random.randrange(0,10),random.randrange(0,10)])

    for n in liste_attente: #on parcours la liste_attente
        #ici on ne fait que supprimer les doublons
        if n in new_liste : 
         pass    
        else : 
            #notre new_liste clean de doublons
         new_liste.append(n)
    
    # pour chaque couple (position_ascenseur, position_personne)
    for [n,m] in new_liste : 
        go_ascenseur(n,m)
        # input va nous servir d'un bouton d'appel et une condition pour démarer notre boucle
appeler_ascenseur = input("pour appeler l'ascenseur, entrez A !")  
while(appeler_ascenseur == 'a' or appeler_ascenseur == 'A'):
        #je simule ici la disponibilité (0=false = pas dispo et 1=true=dispo)
       disponibilite(random.randrange(0,2))
       #pour redémarer notre boucle à chaque fois faut entrer 'A'
       appeler_ascenseur = input("pour appeler l'ascenseur, entrez A !") 
