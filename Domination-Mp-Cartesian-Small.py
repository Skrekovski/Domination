from __future__ import print_function
from multiprocessing.dummy.connection import families
import sys
from sage.all import *
from random import *

#-------------------------------------------------
# MP product

def CartesianProductE(G,H):
    CP_edges=[]
    for x in G.vertices():
        for (a,b) in H.edges(labels=False):
            CP_edges=CP_edges + [((x,a),(x,b))]
    for x in H.vertices():
        for (a,b) in G.edges(labels=False):
            CP_edges=CP_edges + [((a,x),(b,x))]        
    return CP_edges 

def DirectProductE(G,H):
    DP_edges=[]
    for (x,y) in G.edges(labels=False):
        for (a,b) in H.edges(labels=False):
            DP_edges=DP_edges+[((x,a),(y,b)),((x,b),(y,a))]
    return DP_edges    

# Direct co Direct 
def DcDE(G,H):
    return DirectProductE(G,H)+DirectProductE(G.complement(),H.complement())

# Modular product
def MPE(G,H):
    return DcDE(G,H) + CartesianProductE(G,H)

def TestVizing(G,H):
    DG=len(G.dominating_set(total=False))
    DH=len(H.dominating_set(total=False))
    GH=Graph(MPE(G,H))
    DGH=len(GH.dominating_set(total=False))
    ratio=(DG*DH)/(DGH)
    print ("ratio=", ratio)
    if ratio<1:
        print ("Bingo")
        print ()




# -------- SEARCH
def Search():
    global G, DG

    i=0
    for line in sys.stdin:
        i=i+1
        H=Graph(line) 
        DH=len(H.dominating_set(total=False))
        GH=Graph(MPE(G,H))
        DGH=len(GH.dominating_set(total=False))
        ratio=(1.0*DG*DH)/(DGH)
        print ("ratio=", ratio)
        if ratio<1:
            print ("Bingo   ",H.graph6_string(), DH, DGH)
        sys.stdout.flush() 
    print ("\n --- The End ---", i)
    sys.stdout.flush()        


print ("Start:")
a=int(sys.argv[1])
b=int(sys.argv[2])
G=Graph(strG)
DG=len(G.dominating_set(total=False))
print (G.graph6_string(), DG)
Search()





