from __future__ import print_function
from multiprocessing.dummy.connection import families
import sys
from sage.all import *
from random import *


# -------- SEARCH
def Search():
    global G, E, Colored, C, I, index, k, nedges

    print ("Start:")
    sys.stdout.flush() 
    i=0
    for line in sys.stdin:
        i=i+1
        G=Graph(line)
        diam=G.diameter()
        if diam==2:
            gamma=len(G.dominating_set(total=False))  
            if gamma >=4:
                print (gamma,diam, G.graph6_string())
        sys.stdout.flush() 
    print ("\n --- The End ---")
    sys.stdout.flush()        
Search()





