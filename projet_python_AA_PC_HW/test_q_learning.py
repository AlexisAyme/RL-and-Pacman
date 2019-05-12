# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:47:23 2019

@author: aymea
"""

from Q_learning import *

import unittest
from Value_fonction import Value_iterative
import numpy as np 

class RandomTest(unittest.TestCase):
    def test_Q_learning (self):
        # definition d'un env simple 
        n=20
        A =[{}]+[{1,2} for i in range(1,n-1)] + [{1}]
        R= np.array([[0,-i,-i] for i in range (n)])
        T =np.zeros([n,3,n])
        T[n-1,1,n-2]=1
        for i in range (1,n-1):
            T[i,1,i-1]=1
            T[i,1,i+1]=0
            T[i,2,i-1]=0
            T[i,2,i+1]=1
        p=[1]*n
        m=3
        gamma=1   
        Env=Environnement(T,R,A,m,gamma)
        
        # test pour alpha=0.2 et eps =0.2 
        
        QL= Q_learning(env,0.2,0.2)
        
        
        for i in range (100000):
            s = QL.choose_next_state()
            if s>0 : 
                sp= QL.apprendre_action(s)
        
        pi = QL.politique()
        
        for i in range (1,n): 
            self.assertEqual (pi[i] ,1.)
            
if __name__ == '__main__':
    unittest.main()

    
