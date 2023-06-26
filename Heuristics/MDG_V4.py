#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 12:48:47 2022

@author: nathanwilliams
"""

import networkx as nx
import time
from operator import itemgetter


def MDG(G):
    """
    Parameters
    ----------
    G : Graph

    Returns
    -------
    len(C): integer
        The Total Number of Vertices in Minimum Vertex Cover
    C : list
        An Approximation of the Minimum Vertex Cover

    """ 
    # Initialize cover solution
    C = []
    
    # MDG Algorithm
    while len(G.edges) != 0:

        # Determine which vertex has the maximum degree
        max_degree_vertex = max(G.degree, key = itemgetter(1))[0]
        
        # Remove node from the graph
        G.remove_node(max_degree_vertex)
                
        # Add vertex to cover solution
        C.append(max_degree_vertex)

    return len(C), C 


def relative_error(opt, alg):
    """
    Parameters
    ----------
    opt : int
        Optimal Solution.
    alg : int
        Algorithm Solution.

    Returns
    -------
    x : float
        Relative Error.

    """
    x = (alg - opt)/opt
    
    return round(x,6)

graph_dict = {"jazz": 158,"karate": 14,"football": 94,"as-22july06": 3303, "hep-th": 3926, 
              "star": 6902, "star2": 4542, "netscience": 899, "email": 594, "delaunay_n10": 703,
              "power": 2203}


for q in graph_dict:
    print(q + ".graph")
    graph_file = "Desktop/DATA/" + q + ".graph" # update your file path here
    
    """ Read Data """
    with open(graph_file) as file:
        lines = [[int(float(j)) for j in line.rstrip().split()] for line in file]
    
    n_vertices, n_edges, w = tuple(lines.pop(0))
    
    if len(lines) > n_vertices:
        lines = [lines[i] for i in range(n_vertices)]
    
    edges_dict = {}
    for i in range(len(lines)):
        edges_dict[i+1] = lines[i]
    
    """ Create Graph from Data"""    
    G = nx.Graph(edges_dict)
    t0 = time.time()    
    mvc = MDG(G)
    t1 = time.time() - t0
    
    #print("The approximate minimum vertex cover is: ", mvc) # actual minimum vertex cover list
    print("The approximation has", len(mvc), "vertices")
    print("MDG took ", t1, "seconds")
    print("Relative Error: ", relative_error(graph_dict[q], len(mvc)))
    print()