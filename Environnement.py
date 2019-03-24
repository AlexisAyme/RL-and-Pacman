# -*- coding: utf-8 -*-
"""
Projet de Python de premiere année ENSAE 
Renforcement learning 

Alexis AYME 

20/03/2019

let's go :) 

/"""


import numpy as np

class Environnement :
    """ Première classe quand l'on va utiliser pour simuler un MDP """
    
    """Les états sont représenté par des entier de 0 à n-1 et les action de 0 à m-1 """
    
    def  __init__ (self,T,R,A,m,gamma): 
       """T la matrice de transition, R le vecteur des récompenses et A les ensembles d'action """
       self.m_T = np.copy (T)
       self.m_A = np.copy (A)
       self.m_R = np.copy (R)
       self.m_m=m
       self.m_dim= len (R)
       self.m_gamma = gamma
    
    def dimension(self): 
        return self.m_dim
        
    
    def actions_possibles (self,s):
        """donne la liste des actions possibles de l'état s"""
        return self.m_A[s]
    
    def est_terminal(self,s):
        """indique si l'état s est terminal"""
        return self.m_A[s]=={}
    
    def etat_suivant (self,s,a):
        """Retourne l'état suivant s apres l'action a (aléatoire mais suit la proba T)"""
        u=np.random.random()
        som=0
        for i in range(self.m_dim):
            som+= self.m_T[s,a,i]
            if u<=som :
                return i
            
    
    def récompense(self,s,a):
        """Retourne la récompense suivant s apres l'action a (aléatoire mais suit la proba T)"""
        return self.m_R[s,a]
    
    def trajectoire_aléatoire (self,si,k):
        """donne une trajectoire et les récompenses aleatoire de taille k partant 
        de si construite en choisissant une action au pif """
        if k== 0 or self.est_terminal(si) :
            return [(si,0)]
        else :
            a= np.random.choice(np.array(list(self.m_A[si]))) #choix d'une action au hasard parmi toutes celles qui 
            #sont possibles en si
            sp = self.etat_suivant(si,a)
            r = self.récompense(si,a)
            return [(si,r)]+ self.trajectoire_aléatoire(sp,k-1)
        
        
    
    def trajectoire_aléatoire2 (self,si):
        """donne une trajectoire et les récompenses aleatoire partant de si construite
        en choisissant une action au pif et se terminant
        sur un état terminal"""
        if  self.est_terminal(si) :
            return [(si,0)]
        else :
            a= np.random.choice(np.array(list(self.m_A[si])))
            sp = self.etat_suivant(si,a)
            r = self.récompense(si,a)
            return [(si,r)]+ self.trajectoire_aléatoire2(sp)
        
    def trajectoire_pi (self,si,k,pi):
        """donne une trajectoire et les récompenses de taille k partant de si construite 
        en respectant la politique pi """
        if k== 0 or self.est_terminal(si) :
            return [(si,0)]
        else :
            a= pi[si]
            sp = self.etat_suivant(si,a)
            r = self.récompense(si,a)
            return [(si,r)]+ self.trajectoire_pi(sp,k-1,pi)
        
    def trajectoire_pi2(self,si,pi):
        """donne une trajectoire et les récompenses partant de si construite en respectant
        la politique pi et se terminant
        sur un état terminal"""
        if self.est_terminal(si) :
            return [(0,si,si)]
        else :
            a= pi[si]
            sp = self.etat_suivant(si,a)
            r = self.récompense(si,a)
            return [(r,si,sp)] + self.trajectoire_pi2(sp,pi)  




            
            
        







