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

# -------- SEARCH
def Search():
    global G, E, Colored, C, I, index, k, nedges

    print ("Start:")
    sys.stdout.flush() 
    i=0
    for line in sys.stdin:
        i=i+1
        a=1
        G=Graph(line)  
        BigPD(G,a)
        sys.stdout.flush() 
    print ("\n --- The End ---")
    sys.stdout.flush()        
Search()





