#!/usr/bin/python

import sys
import subprocess
from subprocess import Popen
import os
from subprocess import call
import shlex
import numpy as np


def crossmodularity (A,B,alpha,beta,T):
    ############################
    # Given two input (symmetrical) matrices A and B, this function
    # calculates the crossmodularity index X
    # Input's description:
    # A and B are squared matrices of N*N (typically connectivity matrices), being N the number of ROIs
    # alpha and beta are two artibitrary thersholds to binarize the two  matrices (necessary for the similarity calculation)
    # T is the label vector: each element vector is defined as an integer corresponding to the module that ROI belongs to
    # Output's description:
    # X crossmodularity
    # Qa and Qb are modularities of inA and inB associatted to partition T
    # L is the similarity between A and B
    # Ibai Diez. Biocruces Health Research Institute, Spain
    # Please, cite this reference if you use it
    # Diez, I. et al. A novel brain partition highlights the modular skeleton shared by structure and function.
    # Sci. Rep. 5, 10532; doi: 10.1038/srep10532 (2015).
    ###################################
    T = np.asarray(T)
    
    #Get the different labels of the modules
    labels = np.unique(T)
    
    #For each module compute sorensen index
    sorensen = np.zeros(1,length(labels))
    indx_m = np.array()
    for m in range (length(labels)):
        #Select the rois of each module and binarizes the resulting matrices using alpha and betha
        indx = np.where(T==labels[m],True)
        bin_A = A[indx,indx]>alpha
        bin_B = B[indx,indx]>beta
        if length (indx)==1:
            continue
        sorensense [m] = np.sum (2*(np.multiply(bin_A,bin_B)))/(np.sum(bin_A)+np.sum(bin_B))
        indx_m = np.concatenate ((indx_m, m), axis = 1) 
        
     #The total similarity is the mean similarity of all the modules
    L = np.mean(sorensen[indx_m])
    
    #Compute the modularity index
    Qa = modularity_index(np.absolute (A),T)
    Qb = modularity_index(np.absolute (B),T)
    
    #Compute the cross modularity
    X = np.power ((np.multiply(np.multiply (Qa,Qb),L)), 1/3)
    
def modularity_index (A,T):
#A newman spectral algorithm adapted from the brain connectivity toolbox. 
#Original code in here  https://sites.google.com/site/bctnet/measures/list 
    T = np.asarray(T)
    A = np.asarray(A)
    
    N = np.amax (np.shape(A))                       #number of vertices
    K = np.sum(A, axis = 0)                         #degree
    m = np.sum(K, axis = 0)                         #number of edges (each undirected edge is counted twice)
    B = A - (np.dot (np.transpose (K), K)) / m      # modularity matrix
    
    if T.shape [0] == 1:
        T=np.transpose (T)

    s =  T [:, np.ones((1,N))]                        #compute modularity
    Q = np.not_equal (np.multiply ((s - np.transpose (s)), B) / m) 
    Q = np.sum (Q)
    



    