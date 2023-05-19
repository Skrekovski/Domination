from __future__ import print_function
from multiprocessing.dummy.connection import families
import sys
from sage.all import *
from random import *

#-------------------------------------------------
# MP product

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
    global G, DG, PDG

    i=0
    for line in sys.stdin:
        i=i+1
        H=Graph(line) 
        PDH=PeterinDomination(H,1,2)
        DH=PDH[0]
        GH=G.cartesian_product(H)
        GH.relabel()
        PDGH=PeterinDomination(GH,1,2)
        DGH=PDGH[0]
        ratio=(DG*DH)/(DGH)
        print ("ratio=", ratio)
        if ratio>1:
            print ("Bingo   ",H.graph6_string(), DH, DG, DGH)
            print ("PDH=",PDH)
            print ("PDG=",PDG)
            print ("DG=",DG)
        sys.stdout.flush() 
    print ("\n --- The End ---", i)
    sys.stdout.flush()        


print ("Start:")
strG=str(sys.argv[1])
G=Graph(strG)
PDG=PeterinDomination(G,1,2)
DG=PDG[0]
print (G.graph6_string(), PDG, DG)
Search()





