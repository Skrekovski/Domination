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





# -------- SEARCH
def Search():
    global a,b,c

    print ("Start:")
    Table_Str=[]
    for line in sys.stdin:
        Table_Str.append(line)
    print ("Number of graphs =", len(Table_Str))    
    for i in range(a,b):
        G=Graph(Table_Str[i])
        for j in range(i,c): 
            H=Graph(Table_Str[j])   
            MpG=Graph(MPE(G,H))
            DcDG=Graph(DcDE(G,H))
            D=MpG.dominating_set(total=False)
            print ("i,j=",i,j,"Gamma=", len(D))
            #if len(D)==4:
            #    print("Bingo   ",G.graph_string(), H.graph6_string(), len(D))
            #sys.stdout.flush() 
            if len(D)>=5:
                print("Bingo   ",G.graph_string(),H.graph6_string(), len(D))
            Dc=DcDG.dominating_set(total=False)
            print ("i,j=",i,j,"Gammac=", len(Dc))
            if len(D)>=6:
                print("Bingoc   ",G.graph_string(),H.graph6_string(), len(Dc))
            sys.stdout.flush() 



    print ("\n --- The End ---", i)
    sys.stdout.flush()        

a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
Search()





