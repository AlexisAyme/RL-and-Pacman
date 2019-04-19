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



def norme (X):
    """Donne le carré de la norme euclidienne du vecteur X"""
    return sum (X*X)

class Value_iterative :
    def __init__ (self,T,A,R,gamma):
        self.m_T = np.copy (T)
        self.m_A = np.copy (A)
        self.m_R = np.copy (R)
        self.m_gamma = gamma
        
    def f (self, V):
        """La fonction donnée par l'équation de Bellman sur la value fonction retourne f(V) et la politique choisi"""
        n=len(V)
        resV =np.zeros(n)
        pi=np.zeros(n)
        for i in range (n):
            m= 0
            b= False 
            for a in self.m_A[i]:
                S= self.m_R[i,a] + self.m_gamma*sum ([(self.m_T[i,a,j]*V[j]) for j in range(n)])
                if m< S or b==False :
                    m=S 
                    b=True
                    pi[i]=a
            resV[i]= m
        return (resV,pi)
    
    def V_and_pi_star (self,epsilon): 
        """Itération de f pour converger vers le point fixe"""
        n=len(self.m_A)
        V = np.zeros(n)
        (Vp,pi_res) = self.f(V)
        while norme (V-Vp)> epsilon :
            W=Vp
            (Vp,pi_res)=self.f(Vp)
            V=W
        return (Vp,pi_res)   
    

    




class BellmanOperator :
    def __init__ (self,T,A,R,gamma):
        self.m_T = np.copy (T)
        self.m_A = np.copy (A)
        self.m_R = np.copy (R)
        self.m_gamma = gamma
    
    def dimension (self):
        return len(self.m_R)
        
    def TPi_op (self,V,pi):
        """Operateur de Bellman pour une politique pi"""
        n=len(V)
        resV =np.zeros(n)
        for i in range (n):
            resV[i]= self.m_R[i,pi[i]] + self.m_gamma*sum ([(self.m_T[i,pi[i],j]*V[j]) for j in range(n)])      
        return resV
    
    def T_op (self, V):
        """Opérateur dynamique de Bellman retourne aussi la politique utilisée """
        n=len(V)
        resV =np.zeros(n)
        pi=np.zeros(n)
        for i in range (n):
            m= 0
            b= False 
            for a in self.m_A[i]:
                S= self.m_R[i,a] + self.m_gamma*sum ([(self.m_T[i,a,j]*V[j]) for j in range(n)])
                if m< S or b==False :
                    m=S 
                    b=True
                    pi[i]=a
            resV[i]= m
        return (resV,pi)

def PointFixe (op,epsilon,n): 
        """Itération de op  pour converger vers le point fixe avec une précision epsilon en dimension n"""
        V = np.zeros(n)
        (Vp,pi_res) = op(V)
        while norme (V-Vp)> epsilon :
            W=Vp
            (Vp,pi_res)=op(Vp)
            V=W
        return (Vp,pi_res)
    
    
class TDlambda :
    def __init__ (self,ld,env,n_episode):
        self.m_ld =ld
        self.m_env=env
        self.n_ep =n_episode
        self.gamma =
