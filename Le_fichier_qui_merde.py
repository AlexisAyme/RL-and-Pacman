# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:36:02 2019

@author: Philmedion
"""


import numpy as np

from Environnement import *
print("fichier ok")
from TDlambda import *
print("fichier ok")
from Value_fonction import *
print("fichier ok")

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


    
env = Environnement(T,R,A,2,1)
p = [1]*n

VI= Value_iterative(T,A,R,1)
VI.V_and_pi_star(0)

TD = TDlambda(1,env,p)

TD.learn(1000)
    
#on remarque que ca a tendance à donner des vaeurs etranges sur le bord (les valeurs remontent). Ceci est sans doute du au fait que ces 
#etats sont bien moins frequents / sont bien moins utilises en tant qu'etat initial