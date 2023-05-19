from __future__ import print_function
from multiprocessing.dummy.connection import families
import sys
from sage.all import *
from random import *

# -------- SEARCH
def Search():
    for line in sys.stdin:  
        H=Graph(line) 
        if H.diameter()!=2:
            continue
        if (max([H.degree(v) for v in H.vertices()])==H.order()-1):
            continue    
        print(H.graph6_string())        
Search()





