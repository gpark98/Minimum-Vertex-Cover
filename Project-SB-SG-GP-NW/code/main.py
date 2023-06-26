'''
Main file for the project.

Authors:

    -   Sasha M. Bakker
    -   Sebastian Gutierrez Hernandez
    -   Gyujing Park
    -   Nathan B. Williams

This file contains

'''

from genetic_algorithm_v5 import genetic_algorithm_min_vertex_opt
from BnB import BnB
from MDG_final import MDG, read_graph, write_files
from hill_climbing import hill_climbing_opt
from read_data import read_data_graph
from write_results import write_results
import sys
import multiprocessing
import time 

def main(argv):

    file = argv[0]

    graph_name = file.split('.')[0]

    method = argv[1]

    max_time = int(argv[2])

    random_seed = int(argv[3])

    n_vertex,num_edges_G,G = read_data_graph(file)

    if method == 'BnB':

        k,V,time_update,vertex_cover_update = BnB(G, max_time)
        write_results(graph_name,method,max_time,random_seed,V,time_update,vertex_cover_update,k)

    if method == 'Approx':

        G = read_graph(file)

        k, V, time_update = MDG(G, max_time)

        write_files(graph_name, k, V, max_time)


        
    if method == 'LS1':

        k,V,time_update,vertex_cover_update = hill_climbing_opt(G, random_seed, max_time)
        write_results(graph_name,method,max_time,random_seed,V,time_update,vertex_cover_update,k)


    if method == 'LS2':

        # define the total iterations 
        n_iter = 1000
        # bits
        n_bits = n_vertex
        # Pop size
        n_pop = 250
        # Crossover rate
        r_cross = 0.9
        # mutation rate
        r_mut = 0.25

        k,V,time_update,vertex_cover_update =  genetic_algorithm_min_vertex_opt(n_bits,n_iter,n_pop,r_cross,r_mut,num_edges_G,G,random_seed,max_time)

        write_results(graph_name,method,max_time,random_seed,V,time_update,vertex_cover_update,k)  



if __name__ == "__main__":
    
    main(sys.argv[1:])