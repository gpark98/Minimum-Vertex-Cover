#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:29:36 2022

@author: sashabakker
"""

from math import floor, ceil
from copy import copy, deepcopy
from timeit import default_timer as timer
import networkx as nx


def max_degree(G):
    
    vertex_degree = dict(G.degree(G.nodes()))
    node = max(vertex_degree, key=vertex_degree.get)
    max_deg = vertex_degree[node]
    
    return node, max_deg

def neighbors_list(G, v):
    
    return list(G.neighbors(v))
    

def remove_neighborhood(G, v):
    
    neighbors = neighbors_list(G, v)
    for neighbor in neighbors:
        G.remove_node(neighbor)
        
    return G, neighbors

def degLB(graph):
    
    G = graph.copy()
    degrees = []
    n_edges = copy( G.number_of_edges() )
    
    
    while sum(degrees) < n_edges:
        
        node, max_deg = max_degree(G)
        degrees.append(max_deg)
        G.remove_node(node)

    i = len(degrees)
    
    node, max_deg = max_degree(G)
    edges_prime = G.number_of_edges()
    
    if int(edges_prime) == 0:
        frac = 0
    else:
        frac = edges_prime / max_deg
    
    return floor( i + frac )
     

graph_file = "jazz.graph" #"test.txt" #"jazz.graph" #"sasha.txt" #"karate.graph"

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



# Initialize variables
cover = []
frontier = [(cover, G)]
best = (G.number_of_nodes(), (cover, G))

iteration= 0

while len(frontier) != 0:
    
    cover_prime, G_prime = frontier.pop()
    
    v, deg = max_degree(G_prime)
    
    states = [1, 0]
    
    for state in states:
        
        G_bar = G_prime.copy()
        cover_bar = deepcopy(cover_prime)
        
        if state == 1:
            # vertex in cover
            G_bar.remove_node(v)
            cover_bar.append(v)
        
        elif state == 0:
            # vertex not in cover
            G_bar, neighbors = remove_neighborhood(G_bar, v)
            for neighbor in neighbors:
                cover_bar.append(neighbor)
        
        if G_bar.number_of_edges() == 0:
            
            if len(cover_bar) < best[0]:
                
                best = (len(cover_bar), (cover_bar, G_bar))
        
        elif len(cover_bar) + degLB(G_bar) < best[0]:
            
            frontier.append((cover_bar, G_bar))
            
print("\n\nMVC: ", best[0])              


























            
    
            
