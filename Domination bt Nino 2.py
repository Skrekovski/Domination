#!/usr/bin/env sage
from sage.all import *
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

if __name__ == '__main__':

	g6str = 'Cy'
	g6str = 'O?YuA@emuWG_@_Ao@_?G?'
	g6str = ':]c?A`b_Bbi@_I`EmCdE_@DFIfHKNnpjRbDgINQiJNRuaCHPTkM_GMOSeGJLOdE' # order 30, 3m15.670s
	g6str = 'X??????????????????????????????????????F~w?^w^~~N~q' # order 25, 3.497s
	g6str = 'S????????????????????o?B}?Fr~n~~C' # order 20, 1.480s
	
	g = Graph(g6str)
	# h = g.cartesian_product(g)

	ds = domination_sequence(g)
	gc.collect()
	print(ds)

