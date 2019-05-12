# -*- coding: utf-8 -*-
"""
Projet de Python de premiere année ENSAE 
Renforcement learning 

Alexis AYME
Philippe Cantrelle
Hélène Wang 

20/03/2019

/"""

import numpy as np
class TDlambda :
    """ TD lamda algorithm using MC at the first read"""
    
    def __init__ (self,ld,env, pi ):
        n= env.m_dim 
        self.dim = n 
        self.ld =ld
        self.env=env
        self.pi=pi
        self.gamma = env.m_gamma
        self.V= np.zeros(n)
        self.k_step = 1
        self.occ = [1 for i in range (n)]
        
    
    def choose_next_state (self):
        
        n= len(self.occ)
        s= sum(self.occ)
        tab = np.array([s for i in range(n)])- np.array(self.occ)
        som=tab[0]
        u= np.random.random() * s *(n-1)
        i=0
        while som<u :
            i += 1
            som += tab[i]       
        return i
    
    def delta(self,  r, x, xp ) :
        return r + self.gamma*self.V[xp]-self.V[x]
    
    def learn_episode (self,trajectoire):
        z = np.zeros(self.dim)   # trace d'élligibilité 
        Vp= self.V
        for (r,x,xp) in trajectoire :
            z*= self.ld*self.gamma
            z[x]+=1
            delta = self.delta (r,x,xp)
            Vp +=  (1/self.k_step)*delta*z
            
            
        
        self.k_step +=1
        self.V= Vp
        
    def learn (self,n_episode):
        for k in range (n_episode):
            si= self.choose_next_state()
            self.occ[si]+=1
            trajectoire= self.env.trajectoire_pi2 (si,(self.pi))
            self.learn_episode (trajectoire)
        return self.V

