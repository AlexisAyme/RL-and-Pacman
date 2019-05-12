# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:19:23 2019

@author: aymea
"""


from Environnement import *
import numpy as np 



class Q_learning : 
    """ Algorithme de Q learning avec une politique epsilon greedy """
    
    def __init__ (self,env,alpha, epsilon ):
        self.alpha= alpha
        self.env=env
        self.n=env.m_dim
        self.m=env.m_m
        self.occ = [1 for i in range (self.n)]
        self.Q= np.zeros((self.n,self.m+1))
        self.epsilon= epsilon 
        
        
        
    
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
        self.occ[i] += 1
        return i
    
    def max_action(self,s):
        ac=0
        v=- np.inf 
        for a in self.env.actions_possibles(s):
            if v< self.Q[s,a]: 
                ac=a
                v= self.Q[s,a]
        return  ac
    
    def epsilon_greedy(self,s):
        if np.random.rand()< self.epsilon :
            lst= [a for a in self.env.actions_possibles(s)]
            return lst[np.random.randint(len(lst))]
        else :
            return self.max_action(s)
        
        

    def apprendre_action(self,s):
        a= self.epsilon_greedy(s)
        sp = self.env.etat_suivant (s,a)
        r = self.env.récompense(s,a)
        if not (self.env.est_terminal(sp)):
            self.Q[s,a] +=  self.alpha*(r + max ([self.Q[sp,ap] for ap in self.env.actions_possibles(sp)]) - self.Q[s,a] )
        else :
            self.Q[s,a] +=  self.alpha*(r-self.Q[s,a])
        return sp
    
    
    def politique(self):
        pi= np.zeros((self.n))
        for i in range (self.n):
            if not( self.env.est_terminal(i)): 
                pi[i] = self.max_action(i)
        return pi


            
class Q_learning2 (Q_learning):
    """ Q_learning avec comme une politique d'exploration softmax """
    def softmax(self,s):
        lst=[a for a in self.env.actions_possibles(s)]
        exp = np.exp(np.array([self.Q[s,a] for a in lst]))
        S= np.sum(exp)
        exp = exp/S
        alea =np.random.rand()
        u =0
        for i in range (len(lst)):
            u+= exp[i]
            if u> alea :
                return lst[i ]
            
    def apprendre_action(self,s):
        a= self.softmax(s)
        sp = self.env.etat_suivant (s,a)
        r = self.env.récompense(s,a)
        if not (self.env.est_terminal(sp)):
            self.Q[s,a] +=  self.alpha*(r + max ([self.Q[sp,ap] for ap in self.env.actions_possibles(sp)]) - self.Q[s,a] )
        else :
            self.Q[s,a] +=  self.alpha*(r-self.Q[s,a])
        return sp
        