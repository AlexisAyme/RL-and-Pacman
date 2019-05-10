# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:04:23 2019

@author: aymea
"""


import unittest
from Value_fonction import Value_iterative
import numpy as np 

class RandomTest(unittest.TestCase):
    def test_Value_Fonction (self):
        
        # definition d'un env simple 
        n=20
        A =[{}]+[{1,2} for i in range(1,n-1)] + [{1}]
        R= np.array([[0,-i,-i] for i in range (n)])
        T =np.zeros([n,3,n])
        T[n-1,1,n-2]=1
        for i in range (1,n-1):
            T[i,1,i-1]=0.75
            T[i,1,i+1]=0.25
            T[i,2,i-1]=0.25
            T[i,2,i+1]=0.75
        
        #execution de la fonction 
        VI= Value_iterative(T,A,R,1)
        V,Pi = VI.V_and_pi_star(0) 
        self.assertEqual (Pi[16] ,1.)

if __name__ == '__main__':
    unittest.main()