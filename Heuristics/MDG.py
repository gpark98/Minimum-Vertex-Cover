#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 22:06:08 2022

@author: nathanwilliams
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import operator
import random
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
            
            # # Remove node from dictionary of degrees
            # dict_degree.pop(v_degree)
        
        return cover


results = {}
results["jazz"] = []
results["karate"] = []
results["football"] = []
results["as-22july06"] = []
results["hep-th"] = []
results["star"] = []
results["star2"] = []
results["netscience"] = []
results["email"] = []
results["delaunay_n10"] = []
results["power"] = []

print(results)


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

# degrees = sorted((d for n, d in G.degree()), reverse = True)
# max_degree = max(degrees)
# print(max_degree)
# print(np.log(max_degree)+0.57)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()

mvc = MDG(G)
#print()
#print("The approximate minimum vertex cover is: ", mvc)
#print("The approximation has", len(mvc), "vertices")

t1 = time.time() - t0
results["jazz"].append(len(mvc))
results["jazz"].append(t1)
#print("MDG took ", round(t1,3), "seconds")


t0 = time.time()
G = nx.Graph()

filename = "Desktop/DATA/karate.graph"

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

# degrees = sorted((d for n, d in G.degree()), reverse = True)
# max_degree = max(degrees)
# print(max_degree)
# print(np.log(max_degree)+0.57)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()

mvc = MDG(G)
#print()
#print("The approximate minimum vertex cover is: ", mvc)
#print("The approximation has", len(mvc), "vertices")

t1 = time.time() - t0
results["karate"].append(len(mvc))
results["karate"].append(t1)
#print("MDG took ", round(t1,3), "seconds")


t0 = time.time()
G = nx.Graph()

filename = "Desktop/DATA/football.graph"

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

# degrees = sorted((d for n, d in G.degree()), reverse = True)
# max_degree = max(degrees)
# print(max_degree)
# print(np.log(max_degree)+0.57)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()

mvc = MDG(G)
#print()
#print("The approximate minimum vertex cover is: ", mvc)
#print("The approximation has", len(mvc), "vertices")

t1 = time.time() - t0
results["football"].append(len(mvc))
results["football"].append(t1)
#print("MDG took ", round(t1,3), "seconds")

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
        print()

# degrees = sorted((d for n, d in G.degree()), reverse = True)
# max_degree = max(degrees)
# print(max_degree)
# print(np.log(max_degree)+0.57)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()

mvc = MDG(G)
#print()
#print("The approximate minimum vertex cover is: ", mvc)
#print("The approximation has", len(mvc), "vertices")

t1 = time.time() - t0
results["as-22july06"].append(len(mvc))
results["as-22july06"].append(t1)
#print("MDG took ", round(t1,3), "seconds")


t0 = time.time()
G = nx.Graph()

filename = "Desktop/DATA/hep-th.graph"

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

# degrees = sorted((d for n, d in G.degree()), reverse = True)
# max_degree = max(degrees)
# print(max_degree)
# print(np.log(max_degree)+0.57)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()

mvc = MDG(G)
#print()
#print("The approximate minimum vertex cover is: ", mvc)
#print("The approximation has", len(mvc), "vertices")

t1 = time.time() - t0
results["hep-th"].append(len(mvc))
results["hep-th"].append(t1)
#print("MDG took ", round(t1,3), "seconds")

t0 = time.time()
G = nx.Graph()

filename = "Desktop/DATA/star.graph"

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

# degrees = sorted((d for n, d in G.degree()), reverse = True)
# max_degree = max(degrees)
# print(max_degree)
# print(np.log(max_degree)+0.57)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()

mvc = MDG(G)
#print()
#print("The approximate minimum vertex cover is: ", mvc)
#print("The approximation has", len(mvc), "vertices")

t1 = time.time() - t0
results["star"].append(len(mvc))
results["star"].append(t1)
#print("MDG took ", round(t1,3), "seconds")

t0 = time.time()
G = nx.Graph()

filename = "Desktop/DATA/star2.graph"

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

# degrees = sorted((d for n, d in G.degree()), reverse = True)
# max_degree = max(degrees)
# print(max_degree)
# print(np.log(max_degree)+0.57)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()

mvc = MDG(G)
#print()
#print("The approximate minimum vertex cover is: ", mvc)
#print("The approximation has", len(mvc), "vertices")

t1 = time.time() - t0
results["star2"].append(len(mvc))
results["star2"].append(t1)
#print("MDG took ", round(t1,3), "seconds")

t0 = time.time()
G = nx.Graph()

filename = "Desktop/DATA/netscience.graph"

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

# degrees = sorted((d for n, d in G.degree()), reverse = True)
# max_degree = max(degrees)
# print(max_degree)
# print(np.log(max_degree)+0.57)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()

mvc = MDG(G)
#print()
#print("The approximate minimum vertex cover is: ", mvc)
#print("The approximation has", len(mvc), "vertices")

t1 = time.time() - t0
results["netscience"].append(len(mvc))
results["netscience"].append(t1)
#print("MDG took ", round(t1,3), "seconds")

t0 = time.time()
G = nx.Graph()

filename = "Desktop/DATA/email.graph"

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

# degrees = sorted((d for n, d in G.degree()), reverse = True)
# max_degree = max(degrees)
# print(max_degree)
# print(np.log(max_degree)+0.57)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()

mvc = MDG(G)
#print()
#print("The approximate minimum vertex cover is: ", mvc)
#print("The approximation has", len(mvc), "vertices")

t1 = time.time() - t0
results["email"].append(len(mvc))
results["email"].append(t1)
#print("MDG took ", round(t1,3), "seconds")

t0 = time.time()
G = nx.Graph()

filename = "Desktop/DATA/delaunay_n10.graph"

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

# degrees = sorted((d for n, d in G.degree()), reverse = True)
# max_degree = max(degrees)
# print(max_degree)
# print(np.log(max_degree)+0.57)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()

mvc = MDG(G)
#print()
#print("The approximate minimum vertex cover is: ", mvc)
#print("The approximation has", len(mvc), "vertices")

t1 = time.time() - t0
results["delaunay_n10"].append(len(mvc))
results["delaunay_n10"].append(t1)
#print("MDG took ", round(t1,3), "seconds")

t0 = time.time()
G = nx.Graph()

filename = "Desktop/DATA/power.graph"

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

# degrees = sorted((d for n, d in G.degree()), reverse = True)
# max_degree = max(degrees)
# print(max_degree)
# print(np.log(max_degree)+0.57)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()

mvc = MDG(G)
#print()
#print("The approximate minimum vertex cover is: ", mvc)
#print("The approximation has", len(mvc), "vertices")

t1 = time.time() - t0
results["power"].append(len(mvc))
results["power"].append(t1)
#print("MDG took ", round(t1,3), "seconds")

print(results)

print()
for i in results:
    print(i, " ---------> ", "Approx: ", results[i][0], " --- ", "Time (s): ", results[i][1])



# Creating Example Graph
# G = nx.Graph()

# nodes = ["A","B","C","D","E","F","G","H"]
# edges = [("A","B"),("B","C"),("B","D"),("D","E"),("E","C"),("C","F"),("C","G"),("E","H")]


# G.add_nodes_from(nodes)
# G.add_edges_from(edges)

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.show()


# print("The approximate minimum vertex cover is: ", MDG(G))

# G2 = nx.Graph()
# nodes = ["A","B","C","D","E","F","G","H"]
# edges = [("A","B"),("A","D"),("A","G"),("A","H"),("B","E"),("C","H"),("B","F"),("C","G"),("B","H")]

# G2.add_nodes_from(nodes)
# G2.add_edges_from(edges)

# nx.draw(G2, with_labels=True, font_weight="bold")
# plt.show()

# print("The approximate minimum vertex cover is: ", MDG(G2))

# G3 = nx.Graph()
# nodes = ["A","B","C","D"]
# edges = [("A","C"),("B","C"),("D","C")]

# G3.add_nodes_from(nodes)
# G3.add_edges_from(edges)

# nx.draw(G3, with_labels=True, font_weight="bold")
# plt.show()

# print("The approximate minimum vertex cover is: ", MDG(G3))

# G4 = nx.Graph()
# nodes = ["A","B","C","D","E"]
# edges = [("A","B"),("B","E"),("C","E"),("D","E")]

# G4.add_nodes_from(nodes)
# G4.add_edges_from(edges)

# nx.draw(G4, with_labels=True, font_weight="bold")
# plt.show()

# print("The approximate minimum vertex cover is: ", MDG(G4))

# #######################################################

# # Testing using random connected graph generator from on
# G5 = nx.fast_gnp_random_graph(15, 0.1, seed=1)
# nx.draw(G5, with_labels=True, font_weight="bold")
# plt.show()
# print("The approximate minimum vertex cover is: ", MDG(G5))

# G6 = nx.fast_gnp_random_graph(8, 0.2, seed=1)
# nx.draw(G6, with_labels=True, font_weight="bold")
# plt.show()
# mvc = MDG(G6)
# print(len(mvc))
# print("The approximate minimum vertex cover is: ", mvc)

# for i in range(2,10):
#     print(i*3,"Nodes")
#     G = nx.fast_gnp_random_graph(i*2, random.uniform(0.3,0.4))
#     nx.draw(G, with_labels=True, font_weight="bold")
#     x = i*3
#     plt.title("%i Nodes" %x)
#     plt.show()
#     mcv = MDG(G)
#     print("The approximate minimum vertex cover is: ", mcv)
#     print()


# for i in range(10):    
#     print(random.uniform(0.0,0.5))

