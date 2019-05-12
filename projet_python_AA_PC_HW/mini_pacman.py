# -*- coding: utf-8 -*-
"""



"""

from Q_learning import *


import numpy as np



"""Toute nos fonctions précedement codée fonctionne avec des entiers, nous 
devons donc si nous travaillons sur des tuples être en mesure de trouver une
 correspondance bijective, ce que nous faisoins avec le changement de base """

def conversion(lst,n):
    """convertie la liste lst en base n en base 10 """
    lst =lst [::-1]
    S= 0
    for c in lst :
        S = n*S +c
    return S
        

class Mini_Pacman :
    def __init__(self,M,ind,fantome) :
        """ Constructeur de la classe, M est la carte (0 pour du vide et 1 pour un mur)
        ind l'emplacement de debut de pacman et fantome celui du fantome """
        self.M=M
        self.n=len(M)
        self.ind_in =ind
        self.fantome_in = fantome 
        self.ind = ind 
        self.fantome =fantome
        self.d_fantome= 1
        
        # variable pour qu'il soit campatible avec la classe Q learning :
        
        self.m_dim = len(M)**4
        self.m_m = 5
    
    def initialiser (self):
        """ re initialise le pacman"""
        self.ind= self.ind_in
        self.fantome=self.fantome_in 
        self.d_fantome = 1
    
    def directions_possibles (self,c):
        """ Donne les directions possibles a partir de la case c (coordonnée),
        1 pour ouest 2 nord 3 sud 4 ouest"""
        n= self.n
        i,j =c 
        res = set() 
        M= self.M
        if j< n- 1 and M[i,j+1]==0 :
            res.add(2)
        
        if i< n- 1 and M[i+1,j]==0 :
            res.add(3)
        
        if 0< j and M[i,j-1]==0 :
            res.add(4)
        
        if 0< i and M[i-1,j]==0 :
            res.add(1)
        return res
    
    def deplacement_ind (self,a): 
        i,j =self.ind
        
        if a==2 :
            self.ind = i,j+1
        
        elif a==3 :
            self.ind = i+1,j
        elif a==4 :
            self.ind = i,j-1
        elif a==1 :
            self.ind = i-1,j
    
    def deplacement_fantome (self,a): 
        i,j =self.fantome
        
        if a==2 :
            self.fantome = i,j+1
        
        elif a==3 :
            self.fantome= i+1,j
        elif a==4 :
            self.fantome = i,j-1
        elif a==1 :
            self.fantome = i-1,j
    
    def affichage (self):
        M= np.copy(self.M)
        M[self.ind]= 5
        M[self.fantome]= 9
        print(M)
    
    def action_fantome(self):
        """ le fantome se deplace dans la meme direction ou 
        une autre une fois sur 5"""
        c =self.fantome
        D = self.directions_possibles(c)
        a1= np.random.randint(5)
        if (self.d_fantome in D) and a1 > 0 : # le fantome change rarement
            # de direction sauf si on l'oblige
            self.deplacement_fantome(self.d_fantome)
        else :
            lst= [d for d in D]
            d = lst[np.random.randint(len(lst))]
            self.deplacement_fantome(d)
            self.d_fantome= d
    
    # les méthode pour rendre la classe compatible avec Q_learning
    def representant (self):
        """donne l'entier qui représente la position de pacman et du fantome"""
        i,j = self.ind
        k,l= self.fantome
        return conversion([i,j,k,l],self.n)
    
    def actions_possibles (self,s):
        return self.directions_possibles(self.ind)
    
    def récompense (self,s,a):
        return 1.
    
    def etat_suivant(self, s,a):
        self.deplacement_ind(a)
        self.action_fantome()
        return self.representant()
    
    def est_terminal(self,s):
        return self.fantome==self.ind

class Mini_Pacman_2 (Mini_Pacman) :
    
    """classe qui hérite de Mini_Pacman, mais où le fantome est à tete chercheuse,
    c'est à dire il poursuit le pacman en suivant le chemin le plus court"""
    
    
    def deplacement(self,c,a):
        i,j = c
        
        if a==2 :
            i,j = i,j+1
        
        elif a==3 :
            i,j= i+1,j
        elif a==4 :
            i,j = i,j-1
        elif a==1 :
            i,j = i-1,j
        return (i,j)
            
    
    def action_fantome(self):
        """ le fantome est cette fois ci a tete chercheuse """
        cible =set([self.ind])
        ep= (0,0)
        d=0
        while d==0 :
            ciblep= cible.copy()
            for c in ciblep :
                A = self.directions_possibles(c)
                for a in A :
                    cp = self.deplacement(c,a)
                    if cp==self.fantome:
                        a,b =c
                        ap,bp= cp
                        i,j= ap -a, bp-b
                        if i== 1 :
                            d= 1
                        elif i==-1 :
                            d=  3
                        elif j==-1:
                            d=  2
                        else :
                            d=  4
                        break
                    else :
                        cible.add(cp)
                if d!= 0: 
                    break
         
        self.deplacement_fantome(d)
        









        
        