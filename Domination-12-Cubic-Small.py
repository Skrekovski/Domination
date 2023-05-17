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


# -------- SEARCH
def Search():
    global G, a, b, gamma

    print ("Start:")
    i=0
    for line in sys.stdin:
        i=i+1
        G=Graph(line)  
        pd,ipd,D= PeterinDomination(G,a,b)
        if ipd >= gamma:
            print (G.graph6_string(),ipd)
        sys.stdout.flush() 
    print ("\n --- The End ---")
    sys.stdout.flush()        

a=int(sys.argv[1])
b=int(sys.argv[2])
gamma=int(sys.argv[3])

Search()





