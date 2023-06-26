#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 22:06:08 2022

@author: nathanwilliams
"""

import networkx as nx
import operator
import time


def MDG(G):
    """
    Parameters
    ----------
    G : Graph

    Returns
    -------
    cover : list
        An Approximation of the Minimum Vertex Cover.

    """
    # Initialize cover solution
    cover = []
          
    # If there are no edges in the graph, the vertex cover is an empty set
    if len(G.edges()) == 0:
        
        return "The Minimum Vertex Cover is an Empty Set"
    
    else:
        
        # MDG Algorithm
        while len(G.edges()) != 0:
            
            # Initialize a dictionary with keys being nodes and values being their degree
            dict_degree = {}
            
            # Populate degree dictionary
            for i in G.nodes():
                dict_degree[i] = G.degree(i)
                    
            # Create ordered dictionary by maximum degree to minimum degree
            max_finder = dict(sorted(dict_degree.items(), key = operator.itemgetter(1), reverse = True))
            
            # Adjacency list of the current Graph
            adj_list = nx.to_dict_of_lists(G)
            
            # Determine the node (key) with the maximum degree
            v_degree = list(max_finder.keys())[0]
            
            # Add that node to the cover solution
            cover.append(v_degree)
            
            # Remove all edges corresponding to that node
            for i in adj_list[v_degree]:
                G.remove_edge(v_degree,i)
                
            # Remove node from graph
            G.remove_node(v_degree) 
        
        return cover


# Example
t0 = time.time()
G = nx.Graph()

filename = "Desktop/DATA/jazz.graph"

with open(filename) as file:
    top_line = file.readline().split(" ")
    
    counter = 1
    for line in file:
        temp = line.rstrip('\n').split(" ")
        temp.pop(len(temp)-1)
        for vertex in temp:
            G.add_edge(int(counter), int(vertex))
        counter += 1
        print()


mvc = MDG(G)
t1 = time.time() - t0
print("The approximate minimum vertex cover is: ", mvc)
print("The approximation has", len(mvc), "vertices")
print("MDG took ", round(t1,3), "seconds")



