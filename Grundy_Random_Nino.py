#!/usr/bin/env sage
from __future__ import print_function
import sys
from sage.all import *
from random import *
import heapq

def domination_sequence(g):
	n = g.order()
	dolzina = [-1 for i in range(1 << n)]
	parent = [None for i in range(1 << n)]
	dolzina[0] = 0
	q = [(0, 0)]
	while len(q) > 0:
		l, mask = heapq.heappop(q)
		if l < dolzina[mask]:
			continue  # Not on turn yet
		for v in range(n):
			# Add vertex v
			nei = sum(1 << u for u in g.neighbors(v))
			nmask = nei | mask
			if nmask != mask and l + 1 > dolzina[nmask]:
				dolzina[nmask] = l + 1
				parent[nmask] = (mask, v)
				heapq.heappush(q, (l + 1, nmask)) 
	vall = sum(1 << x for x in range(n))
	p = vall
	seq = []
	while parent[p] != None:
		p, v = parent[p]
		seq.append(v)
	return seq[::-1], dolzina[vall]


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
        gd2=domination_sequence(G2)[1]
        print ("n1, n2=", n1, n2, "gd1=,gd2=",gd1,gd2)  
        sys.stdout.flush()
        G3=G1.tensor_product(G2)
        G3.relabel()
        gd3=domination_sequence(G3)[1]
        print ("gd3=", gd3)

        if gd1 * gd2 != gd3:
            print ("-----------Bingo----------")
            print ("G1=",G1.graph6_string(),"\nG2=",G2.graph6_string(),"\nG3=",G3.graph6_string())  
            print (gd1,"\n",gd2,"\n",gd3)
            print(G1.to_dictionary(), G2.to_dictionary())
            sys.stdout.flush()


p=0.1+0.2*random()
it = 2000
a,b=3,


print ("Start")
RW()           
print ("End")