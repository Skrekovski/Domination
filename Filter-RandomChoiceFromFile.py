from __future__ import print_function
from multiprocessing.dummy.connection import families
import sys
from sage.all import *
from random import *

#-------------------------------------------------
# MP product



# -------- SEARCH
def DoIt():
    global a

    Table_Str=[]
    for line in sys.stdin:
        Table_Str.append(line)
    table_len = len(Table_Str)      
    for j in range(a): 
        j=randint(0,table_len-1)
        G=Graph(Table_Str[j])   
        print(G.graph6_string())        

a=int(sys.argv[1])
DoIt()
