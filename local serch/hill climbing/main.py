'''
Main file for the project.

Authors:

    -   Sasha M. Bakker
    -   Sebastian Gutierrez Hernandez
    -   Gyujing Park
    -   Nathan B. Williams

'''
from hill_climbing import hill_climbing_opt
from read_data import read_data_graph
from write_results import write_results
import sys
import multiprocessing
import time 



def main(argv):

    file = argv[0]

    method = argv[1]

    max_time = int(argv[2])

    random_seed = int(argv[3])

    n_vertex,num_edges_G,G = read_data_graph(file+'.graph')

    if method == 'BnB':




        return 1

    if method == 'Approx':




        return 1

    if method == 'LS1':

        # no need to assign parameters ahead.

        k,V,time_update,vertex_cover_update = hill_climbing_opt(G, random_seed, max_time)


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

        k,V,time_update,vertex_cover_update =  genetic_algorithm_min_vertex_opt(n_bits,n_iter,n_pop,r_cross,r_mut,num_edges_G,G,random_seed)

        #time.sleep(5)

        #p.terminate()

        #p.join()

    write_results(file,method,max_time,random_seed,V,time_update,vertex_cover_update,k)
    

    

if __name__ == "__main__":
    
    main(sys.argv[1:])