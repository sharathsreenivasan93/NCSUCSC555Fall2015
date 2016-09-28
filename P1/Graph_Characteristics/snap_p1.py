# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:57:10 2015

@author: sreenivasanh
"""

import snap

def calculate():
	G = snap.LoadEdgeList(snap.PUNGraph, "facebook_combined.txt", 0, 1)
	node_count = 0
	f = open("results_p1.txt","w")
	for NI in G.Nodes():
	      node_count = node_count + 1
	f.write("Number of nodes is %d\n" %(node_count))

	edge_count = 0
	for edge in G.Edges():
		edge_count = edge_count + 1
	f = open('results_p1.txt','a')
	f.write("Number of edges is %d\n" %(edge_count))

	Nodes = snap.TIntFltH()
	snap.GetBetweennessCentr(G, Nodes, 1.0)

	for node in Nodes:
	    f.write("Node - %d Centrality - %f\n" %(node, Nodes[node])) 
	Clustering_Coefficient = snap.GetClustCf (G, -1)
	f.write("Clustering coefficient %f\n" %(Clustering_Coefficient)) 

if __name__ == '__main__':
    calculate()