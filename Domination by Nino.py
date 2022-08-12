#!/usr/bin/env sage
from sage.all import *
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

if __name__ == '__main__':

	g6str = 'S????????????????????o?B}?Fr~n~~C' # order 20, 1.480s
	g6str = 'X??????????????????????????????????????F~w?^w^~~N~q' # order 25, 3.497s
	g6str = 'Cy'
	g6str = 'O?YuA@emuWG_@_Ao@_?G?'
	g6str = ':]c?A`b_Bbi@_I`EmCdE_@DFIfHKNnpjRbDgINQiJNRuaCHPTkM_GMOSeGJLOdE' # order 30, 3m15.670s
	
	g = Graph(g6str)
	# h = g.cartesian_product(g)

	ds = domination_sequence(g)
	print(ds)

