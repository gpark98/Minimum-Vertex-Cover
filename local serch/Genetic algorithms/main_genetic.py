'''
Main file for genetic algorithm




'''


import numpy as np
import networkx as nx
from genetic_algorithm_v3 import genetic_algorithm_min_vertex_opt
from read_data import read_data_graph
import sys
# from time import time
import multiprocessing
import time 

def main(argv):

    file = argv[0]

    method = argv[1]

    n_vertex,num_edges_G,G = read_data_graph(file)

    if method == 'genetic':

        # define the total iterations 
        n_iter = 1000
        # bits
        n_bits = n_vertex
        # Pop size
        n_pop = 150
        # Crossover rate
        r_cross = 0.9
        # mutation rate
        r_mut = 0.25  

        random_seed = 10

        p = multiprocessing.Process(target=genetic_algorithm_min_vertex_opt,name="genetic",args=(n_bits,n_iter,n_pop,r_cross,r_mut,num_edges_G,G,random_seed))

        p.start()

        time.sleep(100)

        p.terminate()

        p.join()


if __name__ == "__main__":
    
    main(sys.argv[1:])