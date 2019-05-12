# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:04:23 2019

@author: aymea
"""

## Test unitaire de Value_Fonction. 

# On définit un environnement simple dans lequel on dispose d'un segment constitué de n cases
# (numérotées de 0 à n-1). Les états sont les positions sur le segment, les actions possibles sont se tourner à gauche (actions 1)
# ou bien à droite (action 2), sauf à la dernière case où l'on est obligé de tourner à gauche. L'état 0 est terminal. 
# La meilleure politique dans ce cas devrait être de toujours se positionner à gauche. On vérifie que le résultat concorde bien.

import unittest
from Value_fonction import Value_iterative
import numpy as np 

class RandomTest(unittest.TestCase):
    def test_Value_Fonction (self):
        
        # définition d'un environnement simple 
        n=20
        # Liste des actions
        A =[{}]+[{1,2} for i in range(1,n-1)] + [{1}] 
        # Matrice des récompenses
        R= np.array([[0,-i,-i] for i in range (n)]) 
        # Matrice de transition
        T =np.zeros([n,3,n])
        T[n-1,1,n-2]=1
        for i in range (1,n-1):
            T[i,1,i-1]=0.75
            T[i,1,i+1]=0.25
            T[i,2,i-1]=0.25
            T[i,2,i+1]=0.75
        
        #exécution de la fonction 
        VI= Value_iterative(T,A,R,1) 
        V,Pi = VI.V_and_pi_star(0) 
        self.assertEqual (Pi[16] ,1.)

if __name__ == '__main__':
    unittest.main()
