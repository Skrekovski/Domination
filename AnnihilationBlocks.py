from __future__ import print_function
import sys
from sage.all import *

def Rannum(n):
    return floor(n*random())

def RemoveVertex(G):
    B,CV= G.blocks_and_cut_vertices()
    nCV=[x for x in G.vertices() if not(x in CV)]
    v = nCV[Rannum(len(nCV))]
    G.delete_vertex(v)
    return (G,v)
   
def AddVertex(G,v):
    B,CV= G.blocks_and_cut_vertices()
    Br=B[Rannum(len(B))]
    G.add_vertex(v)
    if random()<0.75:
        G.add_edges([(v,x) for x in Br])
    else:
        G.add_edge((v,Br[Rannum(len(Br))]))    
    return G  
    
def Tweak(G):
    H,w=RemoveVertex(G)
    return AddVertex(H,w) 


def MedSum(L):
    L.sort()
    sL=sum(L)
    sumall=0
    for d in range(len(L)):
        sumall=sumall+L[d]
        if sumall >= sL/2:
            break 
    return d+1
 
def Domination(G,T):
    return len(G.dominating_set(total=T))

def Anhiliation(G):
    return MedSum(G.degree_sequence())     
    
def Fitness(G):
    return Anhiliation(G) +1 - Domination(G,True)


def SA(i,t):
    global n,c,d,BestG, fitBest,ciklus
    
    H=BestG.copy()
    fitH=fitBest
    steps=0
    ciklus=ciklus+1
    while t>=1.0:
        steps=steps+1
        if ciklus >= 31:
            H=graphs.CompleteGraph(n)
            fitH=Fitness(H)    
            ciklus=0 
        Hn=Tweak(H)
        fitHn=Fitness(Hn)
        if fitHn <= fitH or exp(1000.0*(fitH-fitHn)/t)< 1.0/(random()+0.0000001):
            H=Hn.copy()
            fitH=fitHn
            if fitH <= fitBest:
                BestG = H.copy()
                fitBest=fitH
                ciklus=0
                if fitBest <= 0:
                        print ("------------- Bingo ----------:", BestG.graph6_string(), fitBest)
                        if BestG.is_tree()==False:
                            print (" ------------- BingoBingoBigno ----------") 

                
        t=0.975*t   
    print ("Intr=",i, "Best Graph=",BestG.graph6_string(),"Fitness Best=",fitBest, "ciklus=",ciklus)
    sys.stdout.flush()




def SArun():
    global n,BestG, fitBest
    
    it = n*800
    t= 5.0**100
    BestG=graphs.CompleteGraph(n)
    fitBest=Fitness(BestG)
    print ("Start with: n=",n)
    for i in range(it):
        SA(i,t)
        

print ("Version 2: 10.May.2020")
a,b=10,30
ciklus=0
n=int(a+round((b-a)*random()))
SArun()           
print ("------ The End -----")        

