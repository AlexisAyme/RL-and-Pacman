# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:36:02 2019

@author: Philmedion
"""


import numpy as np

A =[{}]+[{1,2} for i in range(1,n-1)] + [{1}]
R= np.array([[0,-i,-i] for i in range (n)])
T =np.zeros([n,3,n])
T[n-1,1,n-2]=1
for i in range (1,n-1):
    T[i,1,i-1]=0.75
    T[i,1,i+1]=0.25
    T[i,2,i-1]=0.25
    T[i,2,i+1]=0.75

n=20

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
    
env = Environnement(T,R,A,2,1)
p = [1]*n

VI= Value_iterative(T,A,R,1)
VI.V_and_pi_star(0)

TD = TDlambda(1,env,p)

TD.learn(1000)
    
#on remarque que ca a tendance à donner des vaeurs etranges sur le bord (les valeurs remontent). Ceci est sans doute du au fait que ces 
#etats sont bien moins frequents / sont bien moins utilises en tant qu'etat initial