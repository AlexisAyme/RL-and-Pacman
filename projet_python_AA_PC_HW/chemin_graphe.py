# -*- coding: utf-8 -*-
"""
Projet de Python de premiere année ENSAE 
Renforcement learning 

Alexis AYME 
Philippe Cantrelle
Hélène Wang 

/"""

import numpy as np 

from Value_fonction import * 

def Graphe2env (M):
    """ A partir d'une matrice adjacente d'un graphe orienté, donne T,A,R pour
    simuler un environnement. Par convention l'état 0 est l'état de départ et l'état n-1 
    celui d'arrivé """
    n= len(M)
    T= np.zeros((n,n,n))
    R= np.zeros((n,n))
    A = [set() for i in range (n)]
    for i in range(n):
        for j in  range(n):
            if M[i,j]> 0 :
                A[i].add(j)
                R[i,j]= - M[i,j]
                T[i,j,j]=1
    return T,A,R

def plus_court_chemin (M): 
    """ Retourne le plus court chemin entre 0 et n-1 """
    n=len(M)
    T,A,R = Graphe2env(M)
    VI= Value_iterative(T,A,R,1)    
    V,Pi= VI.V_and_pi_star(0.1)         
    res= [0]
    point = 0
    while point!=n-1 : 
        pp= int(Pi[point])
        res.append(pp)
        point=pp
    return (-V[0], res)





