## Test unitaire des fonctions de la classe Environnement


import unittest

from Environnement import *

import numpy as np


class TestEnvironnement(unittest.TestCase):
    
    '''On teste les fonctions de la classe Environnement'''
    
    def test_environnement(self):

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
        
        # Test de actions_possibles
        i=np.random.randint(1,n-1)
        a=Env.actions_possibles(i)
        b=Env.actions_possibles(0)
        c=Env.actions_possibles(n-1)
        self.assertEqual((a,b,c),({1,2},{},{1}))
          
        # Test de test_est_terminal
        self.assertEqual(Env.est_terminal(0),True)
        
        #Test de trajectoire_pi2
        t1=Env.trajectoire_pi2(n-1,p)
        t2=[(1+i-n,n-1-i,n-i-2) for i in range(n-1)]+[(0,0,0)]
        self.assertEqual(t1,t2)
          
            
if __name__ == '__main__':
    unittest.main()
            