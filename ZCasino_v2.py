# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:23:38 2018

@author: Fantasya
"""

""" 
Jeux de roulettes : 50 nombres de 0 à 49. 

Condtions de victoire :
    
    - numéro gagnant = numéro choisi 
        [retour de la mise + 3 fois sa valeur]
        
    - numéro gagnant de même parité que celui choisi
        [retour de la mise + 50% de sa valeur] 
        
Fin du jeu quand le joueur n'a plus d'argent
"""

import math
from random import randrange

range_roulette = 50
encore = True
argent_joueur = -1
cheat_mode = False
chance = 0

while argent_joueur < 0:
    argent_joueur = input("Vous êtes l'heureux possesseur de... de combien d'ailleurs ?\n")
    try:
        argent_joueur = int(argent_joueur)
    except ValueError:
        print("Il faut saisir un nombre, gros malin !")
        argent_joueur = -1;
        continue
    if argent_joueur <= 0:
        print ("On va commencer avec un entier positif d'accord ?")

while argent_joueur > 0 and encore:
#    num_choisi = input("Sur quel numéro souhaitez misez ?")
#    mise = input("Combien souhaitez vous miser ?")
    
    [num_choisi, mise] = [-1, -1]
    while num_choisi < 0 or mise <= 0:       
        try:
            num_choisi, mise = input("Tapez le numéro choisi puis votre mise :\n").split()
            num_choisi = int(num_choisi)
            mise = int(mise)
            if num_choisi not in range(range_roulette):
                print (f"Il faut choisir un nombre entre 0 et {range_roulette} !")
                num_choisi = -1
            if mise <= 0:
                print("Bravo ! Une mise pleine de bon sens...")
            elif mise > argent_joueur:
                print(f"Vous n'avez pas assez d'argent pour une telle mise ! Vous avez {argent_joueur} $")
                mise = -1
        except ValueError:
            print ("Choisissez des nombres (ex :10 20) ! Et les bons...")
            [num_choisi, mise] = [-1, -1]
    
    # Détermination du numéro gagnant
    num_gagnant = randrange(range_roulette)
    
    if cheat_mode:
        num_gagnant = randrange(num_choisi - 25 + chance, num_choisi + 26 - chance) % range_roulette
        
    print ("\nEt c'est le", num_gagnant,"qui sort !\n")
    
    if num_gagnant == num_choisi: 
        print ("Wow !!!\nSacré chance, il faut le dire !")
        argent_joueur += 3*mise
    elif num_gagnant % 2 == num_choisi % 2:
        print ("Un choix de couleur s'étant avéré fort judicieux !")
        argent_joueur += math.ceil(0.5*mise)
        if cheat_mode and chance < 23:
            chance += 1
    else:
        print ("Pas de bol...")
        argent_joueur -= mise
               
    print ("\nVous avez",argent_joueur,"$.\n")
    
    if argent_joueur == 0:
        encore = False
    else:
        encore = (input("On continue ? [o/n]\n"))
        if encore == "Batman":
            cheat_mode = True
            chance = 10
            encore = "o"
        while encore != 'o' and encore != 'n':
            encore = (input("On continue ? (o/n)"))
            print("Veuillez répondre par o ou n")
    
        encore = (encore == 'o')
 
print ("Vous finissez avec",argent_joueur,"$")

if argent_joueur == 0:
    print ("Voilà ce qui arrive quand on a aucune mesure !")    
