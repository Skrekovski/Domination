from __future__ import print_function
from multiprocessing.dummy.connection import families
import sys
from sage.all import *
from random import *

def NoC3NoC5(H):
    dist = H.distance_all_pairs()
    for (u,v) in H.edges():
        good_edge=False
        for x in H.vertices():
            if (dist(u,x)==2 and dist(v,x)==2) or (dist(u,x)==1 and dist(v,x)==1):
                good_edge=True
                continue
        if  good_edge==False:
                return False
    return True






# -------- SEARCH
def Search():
    dist = H.distance_all_pairs()
    for line in sys.stdin:  
        H=Graph(line) 
        for (u,v) in H.edges():
            good_edge=False
            for x in H.vertices():
                if (dist(u,x)==2 and dist(v,x)==2) or (dist(u,x)==1 and dist(v,x)==1):
                    good_edge=True
            if  good_edge==False:
                return False
        return True           



        if H.diameter()!=2:
            continue
        if (max([H.degree(v) for v in H.vertices()])==H.order()-1):
            continue    
        print(H.graph6_string())        
Search()





