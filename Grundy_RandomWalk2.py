from __future__ import print_function
import sys
from sage.all import *
from random import *

# Checking if a new element can be inserted
def Free(v):
    global s, S, VS, US, G
    
    L=[x for x in G.neighbors(v) if x not in US]
    if L==[]:
        return False
    return True

#  after inserting new element in S we expand US  
def ExpandUnion(v):
    global s, S, VS, US, G
    
    for x in G.neighbors(v):
        if x not in US:
            US.append(x)
            
    
#  after removing last element of S we evaluate US from begining   
def ResetUnion():
    global s, S, VS, US, G
    
    US = []  
    for x in S:
        ExpandUnion(x)
        
def GrundingTotalDomination2():
    global G, s, S, VS, US

    bests=0                        # best of the bests 
    bestS=[]

    n=G.order()
    start_vertex=-1
    S=[]; US=[] 
    while start_vertex <= n-1:
        if S==[] and start_vertex == n-1:   # ending
            start_vertex+=1
            continue   
        if S==[]:                 # inicializacija
            start_vertex+=1
            S=[start_vertex]
            US=G.neighbors(start_vertex)
            k=0   
            continue
        if k==n:                            # odstranimo zadnji 
            k=S[len(S)-1]+1 
            S.pop(len(S)-1) 
            ResetUnion()           # nanovo unijo
            continue
        if (k not in S) and Free(k):    # k dodamo v S
            ExpandUnion(k)            
            S.append(k)
            k=0
            if len(S) > bests:
                bests = len(S); bestS = list(S) 
        else:
            k=k+1 
    return bests, bestS               

# ----------------------------------------------------------
def GrundingTotalDominationOld():
    global G, s, S, VS, US

    bests=0                        # best of the bests 
    bestS=[]

    n=G.order()
    start_vertex=-1
    S=[]; US=[]; 
    while start_vertex <= n-1:
        if S==[] and start_vertex == n-1:
            start_vertex+=1
            continue
        if S==[]:
            start_vertex+=1
            #print ("start vertex =", start_vertex)
            S=[start_vertex]
            US=G.neighbors(start_vertex)
            VS=[0 for i in G.vertices()]; VS[start_vertex]=1
            s=1; k=0   
            continue
        if k==n:
            k=S[s-1]+1 
                # odstranimo zadnji
            VS[S[s-1]-1]=0
            S.pop(s-1) 
            ResetUnion()           # nanovo unijo
            s=s-1
            continue
        if Free(k):    # k dodamo v S
            VS[k]=1
            ExpandUnion(k)
            s=s+1
            S.append(k)
            if s > bests:
                bests = s; bestS = list(S) 
        else:
            k=k+1
        #print ("s=",s,"S=",S,"US=",US,"VS=",VS, "start_vrx=",start_vertex, "k=",k, "bestS=", bestS)    
    return bests, bestS         


def StartGraph(p,n):
    G=graphs.RandomGNP(n,p)
    G.add_edges(graphs.RandomTree(n).edges())
    return G
    
def RW():
    global p, it, a, b, n1,n2, G
    
    for i in range(it):
        print ("i=",i)

        n1=int(a+round((b-a)*random()))
        n2=int(a+round((b-a)*random())) 
        G1=StartGraph(p,n1)
        G=G1
        g1=GrundingTotalDomination()

        G2=StartGraph(p,n2)
        G=G2
        g2=GrundingTotalDomination()

        G3=G1.tensor_product(G2)
        G=G3
        G.relabel()
        g3=GrundingTotalDomination()
        sage
        if g1[0] * g2[0] != g3[0]:
            print ("-----------Bingo----------")
            print ("G1=",G1.graph6_string(),"\nG2=",G2.graph6_string(),"\nG3=",G3.graph6_string())  
            print (g1,"\n",g2,"\n",g3)
            print(G1.to_dictionary(), G2.to_dictionary())


p=0.1+0.2*random()
it = 200
a,b=3,10


print ("Start")
RW()           
print ("End")