'''
Main file for genetic algorithm




'''


import numpy as np
import networkx as nx
from genetic_algorithm import genetic_algorithm_min_vertex_opt,cost_cover


'''
Example 
'''

G = nx.Graph()
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,4)
G.add_edge(2,5)
G.add_edge(3,4)
G.add_edge(3,5)
G.add_edge(1,8)
G.add_edge(8,3)
G.add_edge(7,4)
G.add_edge(7,6)
G.add_edge(6,2)
G.add_edge(6,5)



# define the total iterations 
n_iter = 1500
# bits
n_bits = len(G.nodes)
# Pop size
n_pop = 10
# Crossover rate
r_cross = 0.9
# mutation rate
r_mut = 1.0/float(n_bits)
# decision problem 
k = 6
# Entries to crossover < k
n_cross = int(k/2)
# Entries to mutate 
n_mut = 1

num_edges_G =len(G.edges)




print(genetic_algorithm_min_vertex_opt(n_bits,n_iter,n_pop,r_cross,r_mut,n_cross,n_mut,num_edges_G,cost_cover,G))


