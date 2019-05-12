# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:17:40 2019

@author: aymea
"""

from mini_pacman import * 

import time
import matplotlib.pyplot as plt



def graphe(memo,f) :
    iteration = len(memo)
    plt.plot(np.array([i for i in range(iteration)]),memo)
    plt.title("Temps de vie du Pacman en fonction de l'apprentissage ")
    
    plt.show()
    
    # moyenne flotante
    tendance= np.array( [np.median([memo[i]for i in range(j-f,j+f)]) for j in range(f,iteration-f)])
    plt.plot(np.array([i for i in range(f,iteration-f)]),tendance)
    plt.title("Médiane flottante du temps de vie du Pacman en fonction de l'apprentissage ")
    
    
    plt.show()



def entrainement (QL,iteration):
    memo=np.zeros((iteration))
    for i in range(iteration) :
        
        QL.env.initialiser()
        s= QL.env.representant()
        
        while not(QL.env.est_terminal(s)):
            memo [i]+=1 
            s= QL.apprendre_action(s)
    
    plt.plot(np.array([i for i in range(iteration)]),memo)
    
    plt.show()
    
    # moyenne flotante
    tendance= np.array( [sum([memo[i]for i in range(j-20,j+20)])/40 for j in range(20,iteration-20)])
    plt.plot(np.array([i for i in range(20,iteration-20)]),tendance)
    
    plt.show()
    
    

def entrainement_filmé(QL,iteration):
    for i in range(iteration) :
        print("===== debut de la partie numero ",i," =====" )
        QL.env.initialiser()
        s= 144
        while not(QL.env.est_terminal(s)):
            QL.env.affichage()
            time.sleep(1)
            s= QL.apprendre_action(s)







def entrainement_sequence(QL,n_sequence,l_sequence):
    memo=np.zeros((n_sequence*l_sequence))
    for i in range(n_sequence):
        for j in range(l_sequence) :
        
            QL.env.initialiser()
            s= 144
            
            while not(QL.env.est_terminal(s)):
                memo [i*l_sequence + j]+=1 
                s= QL.apprendre_action(s)
        
        print ("========= SEQUENCE numero ", i," ========")
        
        graphe(memo[:i*l_sequence ],200)


def entrainement_sequence_kill(QL,n_sequence,l_sequence,kill):
    """L'individu est kill au bout d'un certain, la neccésité de cette fonction
    viens de situation ou l'apprentissage est tres rapide """
    memo=np.zeros((n_sequence*l_sequence))
    for i in range(n_sequence):
        for j in range(l_sequence) :
        
            QL.env.initialiser()
            s= 144
            
            while not(QL.env.est_terminal(s)) and (memo [i*l_sequence + j]< kill) :
                memo [i*l_sequence + j]+=1 
                s= QL.apprendre_action(s)
        
        print ("========= SEQUENCE numero ", i," ========")
        
        graphe(memo[:i*l_sequence ],200)

