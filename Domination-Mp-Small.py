from __future__ import print_function
from multiprocessing.dummy.connection import families
import sys
from sage.all import *
from random import *

def PeterinDomination(G,a,b):
    dist = G.distance_all_pairs()
    PD = MixedIntegerLinearProgram(maximization = False)
    y = PD.new_variable(binary = True)
    PD.set_objective(sum([y[i] for i in G.vertices()]))
    for v in G.vertices():
        PD.add_constraint(sum([a*y[v]]+[y[i] for i in G.neighbors(v)])>=a)
        PD.add_constraint(sum([(b-G.degree(v))*y[v]]+[y[i] for i in G.neighbors(v)])<=b)
    pd = PD.solve()
    x = PD.get_values(y)
    L=[i for i in G.vertices() if x[i]==1.0]
    return (pd,len(L),L)
    #return (len(L),L)

# a = 1 bo največrkat
def BigPD(G,a):
    maxD=max([G.degree(x) for x in G.vertices()])
    for k in range(1,maxD):
        pd,ipd,D= PeterinDomination(G,a,k)
        if ipd==G.order():
            print (G.graph6_string(), k)       

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
            DP_edges=DP_edges+[((x,a),(y,b)),((x,a),(y,b))]
    return DP_edges    

# Direct co Direct 
def DcDE(G,H):
    return DirectProductE(G,H)+DirectProductE(G.complement(),H.complement())

# Modular product
def MPE(G,H):
    return DcDE(G,H) + CartesianProductE(G,H)





# -------- SEARCH
def Search():
    global G, Total

    i=0
    for line in sys.stdin:
        i=i+1
        H=Graph(line) 
        MpG=Graph(MPE(G,H))
        D=MpG.dominating_set(total=Total)
        print ("Gamma=", len(D))
        if len(D)>=5:
            print("Bingo   ",H.graph6_string(), len(D))
        sys.stdout.flush() 
    print ("\n --- The End ---", i)
    sys.stdout.flush()        


print ("Start:")
strG=str(sys.argv[1])
#print (sys.argv[2])
Total=False
print ("graph6_string=",strG, "\n Total Domination",Total) 
G=Graph(strG)
sys.stdout.flush() 
Search()





