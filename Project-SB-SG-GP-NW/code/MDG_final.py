#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:13:52 2022
@author: nathanwilliams
"""

import networkx as nx
import time
from operator import itemgetter


def MDG(G, time_constraint): # add as input time constraint
    """
    Parameters
    ----------
    G : Graph
        Graph.
    time_constrant: float
        Time Allowed for Algorithm to Run.

    Returns
    -------
    len(C): integer
        The Total Number of Vertices in Minimum Vertex Cover.
    C : list
        An Approximation of the Minimum Vertex Cover.
    t1: string
        The Total Time Needed to Run Algorithm.

    """ 
    # Begin Time
    t0 = time.time()    
    
    # Initialize cover solution
    C = []
    
    # MDG Algorithm
    while len(G.edges) != 0:
        
        if (time.time() - t0) < time_constraint:

            # Determine which vertex has the maximum degree
            max_degree_vertex = max(G.degree, key = itemgetter(1))[0]
            
            # Remove node from the graph
            G.remove_node(max_degree_vertex)
                    
            # Add vertex to cover solution
            C.append(max_degree_vertex)
        
        else:
            
            print("Time Limit Reached")
            
            return len(C), C, time_constraint
    
    t1 = time.time() - t0

    return len(C), C, str(t1)


def read_graph(graph_file):

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
    
    return G


def write_files(graph_name, k, mvc, total_time):
    """
    Parameters
    ----------
    graph_name : Str
        Name of graph.
    k : Int
        Quality of Minimum Vertex Cover Solution.
    mvc : List
        List of Minimum Vertex Cover.
    total_time : Float
        Total Time Needed to Run Algorithm.

    Returns
    -------
    None.
    
    """
    

    file_name = graph_name+'_Approx_'+str(total_time)
    # Write solution file
    f = open(file_name+ ".sol","w+")
    f.write(str(k) + "\n")
    for i in range(k):
        
        v = str(mvc[i])
        
        if i < k - 1:
        
            f.write(v + ", ")
        else:
            f.write(v)
    f.close()
    
    # Write trace file
    f = open(file_name+".trace","w+")
    f.write(str(total_time) + ", " + str(k))
    f.close()

