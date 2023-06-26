'''
Main file for the project.

Authors:

    -   Sasha M. Bakker
    -   Sebastian Gutierrez Hernandez
    -   Gyujing Park
    -   Nathan B. Williams

'''

#from genetic_algorithm_v5 import genetic_algorithm_min_vertex_opt
from main_utils import read_data_graph, write_results
import sys
import multiprocessing
import time 
from BnB import BnB


def main(argv):
    

    file = argv[0] # GRAPH FILE NAME WITHOUT THE .graph EXTENSION

    method = str(argv[1])

    max_time = int(argv[2])

    random_seed = int(argv[3])

    n_vertex,num_edges_G,G = read_data_graph(file+'.graph')

    if method == 'BnB':


        k,V,time_update,vertex_cover_update = BnB(G, max_time)

        return 1

    if method == 'Approx':




        return 1

    if method == 'LS1':




        return 1



    if method == 'LS2':

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

        #p = multiprocessing.Process(target=return_1,args=[])

        #p.start()

        #k,V,time_update,vertex_cover_update =  genetic_algorithm_min_vertex_opt(n_bits,n_iter,n_pop,r_cross,r_mut,num_edges_G,G,random_seed,max_time)

        #time.sleep(5)

        #p.terminate()

        #p.join()

    write_results(file,method,max_time,random_seed,V,time_update,vertex_cover_update,k)
    

    

if __name__ == "__main__":
    
    main(sys.argv[1:])