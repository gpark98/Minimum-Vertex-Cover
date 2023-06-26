#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 23:23:52 2022

@author: nathanwilliams
"""

import networkx as nx
import time

def MDG(G):
    """

    Parameters
    ----------
    G : Graph

    Returns
    -------
    C : list
        An Approximation of the Minimum Vertex Cover

    """
    
    # Initialize cover solution
    C = []
    
    # MDG Algorithm
    while len(G.edges) != 0:

        # Determine which vertex has the maximum degree
        max_degree_vertex = sorted(G.degree, key=lambda x: x[1], reverse=True)[0][0]

        # Remove node from the graph
        G.remove_node(max_degree_vertex)
                
        # Add vertex to cover solution
        C.append(max_degree_vertex)


    return C

t0 = time.time()
G = nx.Graph()

filename = "Desktop/DATA/as-22july06.graph"

with open(filename) as file:
    top_line = file.readline().split(" ")
    
    counter = 1
    for line in file:
        temp = line.rstrip('\n').split(" ")
        temp.pop(len(temp)-1)
        for vertex in temp:
            G.add_edge(int(counter), int(vertex))
        counter += 1


mvc = MDG(G)
t1 = time.time() - t0
#print("The approximate minimum vertex cover is: ", mvc)
print("The approximation has", len(mvc), "vertices")
print("MDG took ", round(t1,3), "seconds")