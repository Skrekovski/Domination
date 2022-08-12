#!/usr/bin/env sage
from __future__ import print_function
import sys
from sage.all import *
from random import *
import heapq
import gc

def domination_sequence(g):
	n = g.order()
	dolzina = dict()
	dolzina[0] = (0, None, None)
	q = [(0, 0)]
	while len(q) > 0:
		l, mask = heapq.heappop(q)
		if l < dolzina.get(mask, (-1, None, None))[0]:
			continue  # Not on turn yet
		for v in range(n):
			# Add vertex v
			nei = sum(1 << u for u in g.neighbors(v))
			nmask = nei | mask
			dnm, _, _ = dolzina.get(nmask, (-1, None, None))
			if nmask != mask and l + 1 > dnm:
				dolzina[nmask] = (l + 1, mask, v)
				heapq.heappush(q, (l + 1, nmask)) 
	vall = sum(1 << x for x in range(n))
	p = vall
	seq = []
	while dolzina[p][2] != None:
		_, p, v = dolzina[p]
		seq.append(v)
	return seq[::-1], dolzina[vall][0]

def StartGraph(p,n):
    G=graphs.RandomGNP(n,p)
    G.add_edges(graphs.RandomTree(n).edges())
    return G
    
def RW():
    global p, it, a, b, n1,n2, G
    
    for i in range(it):
        print ("------ i=",i)
        sys.stdout.flush()

        n1=int(a+round((b-a)*random()))
        n2=int(a+round((b-a)*random())) 
        G1=StartGraph(p,n1)
        G2=StartGraph(p,n2)
        gd1=domination_sequence(G1)[1]
        gc.collect()
        gd2=domination_sequence(G2)[1]
        gc.collect()
        print ("n1, n2=", n1, n2, "gd1=,gd2=",gd1,gd2)  
        sys.stdout.flush()
        G3=G1.tensor_product(G2)
        G3.relabel()
        gd3=domination_sequence(G3)[1]
        gc.collect()
        print ("gd3=", gd3)

        if gd1 * gd2 != gd3:
            print ("-----------Bingo----------")
            print ("G1=",G1.graph6_string(),"\nG2=",G2.graph6_string(),"\nG3=",G3.graph6_string())  
            print (gd1,"\n",gd2,"\n",gd3)
            print(G1.to_dictionary(), G2.to_dictionary())
            sys.stdout.flush()


p=0.1+0.2*random()
it = 2000
a,b=3,7


print ("Start")
RW()           
print ("End")