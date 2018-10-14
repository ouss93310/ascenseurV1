# ascenseurV1
Elevator programmé en python c'est un premier test donc changements à venir au fur et à mesure ! 

pour tester soit on utilise un environnement de développement comme spyder ou si non plus simple : 
Aller sur : https://www.onlinegdb.com/online_python_debugger et on l'execute en ligne. 
----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------
#grossomodo : 

on a ascenseur devant nous : 
on appuie : 
  si dispo -> il vient directement (on fait appelle à notre fonction go-ascenseur qu'on a créé)
   
  si non ->  il invite la personne à attendre son tour :
    -> puis, on simule une liste d'attente créé aléatoirement par la machine ! (on a supposé que beaucoups de personne attendent)
      -> cette liste contient (nouvelle_ascenseur_position, nouvelle_personne_position)
    -> par la suite on parcourt notre liste d'attente et on fournit à chaque fois le couple :
                  (nouvelle_ascenseur_position,     nouvelle_personne_position)
       à notre fonction go_ascenseur. On admet que la priorité va en fonction de la position des couples dans notre liste. 
          [pririoté1,priorité2, ...,prioritéN]
    -> une fois que la liste est parcourue suffit d'appuyer à nouveau sur A pour appeler l'ascenseur ! 
 
---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------


