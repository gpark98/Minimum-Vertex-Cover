'''
Code for the solution of the Minimum Vertex Cover using a genetic algorithm

This code is part of the project by:

Sasha M. Bakker, Sebastian Gutierrez, Gyujin Park and Nathan Williams

This file contains the main functions for the genetic algorithm soluiton 

Functions in the file:

    - crossover_min_vertex_cov

    - mutation_min_vertex_cov

    - genetic_algorithm_min_vertex_decision

    - num_edge_cover

    - cost_cover

To compile this file is necessary to have the libraries:

    - numpy

    - networkx

'''

import numpy as np

import networkx as nx


def selection(pop,n_pop,scores, k = 3):

    #Select first parent
    selection_ix = np.random.randint(n_pop)
    # Randomly pick k-1 parents
    for ix in np.random.randint(0,n_pop,k-1):

        # Compare score of parents and select best score
        if scores[ix] < scores[selection_ix]:

            selection_ix = ix

    return pop[selection_ix]


def num_edge_cover(G,C: list):


    '''
    Function to obtain number of edges covered by C
    Input: C -> Vertex subset 
    Output: count -> int
    '''
    count = 0

    # For every vertex  u in C
    for u in C:
        # Count every conection v
        for v in list(G.adj[u]):
            # Avoid repeting edge (u,v) and (v,u)
            if v in C and v<u:
                continue
            else:
            # Add new edges 
                count +=1
    return count




def cost_cover(num_edges_G: int,C: list,G):

    '''
    Function to asses the fitness of C
    For a vertex cover returns 0 
    Input:
    num_edges_G: Number of edges in graph G
    C: Strings of 1 and 0
    G: graph
    Output:
    Difference between number of edges and edges covered by C.
    '''


    #Obtain subset from binary string
    V = np.where(np.asanyarray(C)==1)[0]+1

    return num_edges_G-num_edge_cover(G,V)


def crossover_min_vertex_cov(p1: list,p2: list,n_cross: int,r_cross: float):
    '''
    Function for doing crossover of partents
    Input:
    p1,p2: parents
    p: integer smaller than current vertex cover decision problem
    r_cross: float for deciding if crossover occurs
    Output:
    c1,c2: lists. Childs of p1 and p2

    '''
    # Given two parents
    # Copy parents
    c1,c2 = p1.copy(),p2.copy()
    # If crossover occures
    if np.random.rand()<r_cross:
        # Select a partition point
        # replace = False. Avoid sampling one number more than once
        idx1 = np.random.choice(np.where(np.asarray(p1)==1)[0],n_cross,replace = False)
        idx2 = np.random.choice(np.where(np.asarray(p2)==1)[0],n_cross,replace = False)
    

        idx1_valid = []
        idx2_valid = []

        # Find subsets of indexes to ensure that there are k 1s in each child
        # Only do a swap when for a 1 corresponds a 0

        for i in range(n_cross):

            if p2[idx1[i]] == 0:

                idx1_valid.append(idx1[i])      

            if p1[idx2[i]] ==0:

                idx2_valid.append(idx2[i])

        # Only swap shared amount of indexes correspondances

        m = min(len(idx1_valid),len(idx2_valid))

        # Randomly select which indexes to change

        idx1 = np.random.choice(idx1_valid,m,replace = False)

        idx2 = np.random.choice(idx2_valid,m,replace = False)

        # Change the indexes

        for i in range(m):

            c1[idx2[i]] = p2[idx2[i]]

            c1[idx1[i]] = 0

            c2[idx1[i]] = p1[idx1[i]]

            c2[idx2[i]] = 0

    return [c1,c2]


def mutation_min_vertex_cov(bitstring: list,n_bits: int,n_mut: int,r_mut: float, k :int):
    # Given a bitstring
    # Go through each elemnt of the string
 

    if np.random.rand() < r_mut:
        if n_mut< k and n_mut< n_bits-k:

            idx1 = np.random.choice(np.where(np.asarray(bitstring)==1)[0],n_mut,replace = False)

            idx0 = np.random.choice(np.where(np.asarray(bitstring)==0)[0],n_mut,replace = False)

            

            for i in range(n_mut):

                bitstring[idx0[i]] = 1

                bitstring[idx1[i]] = 0

    return bitstring

# genetic algorithm
def genetic_algorithm_min_vertex_decision(n_bits: int , n_iter: int, n_pop: int, r_cross: float,r_mut: float,n_cross : int ,n_mut: int ,k: int,num_edges_G: int,objective, G):
    '''
    Input:

    objective: function that has two parameters num_edges_g and bitstring c

    n_bits: length of population element

    n_iter: number of iterations for the genetic algorithm

    n_pop: number of elements in the population

    r_cross: parameter to determine if a crossing occurs or not

    r_mut: parameter to determine if a mutation occurs or not

    n_cross: maximum number of entries exchanged in a cross over requirement n_cross<k

    n_mut: maximum number of entries mutated, requirement n_mut <k and n_mut<n_bits-k

    k: Decision problem, is there a vertex cover of size k?

    num_edges_g: number of edges in graph G.

    G: graph


    Output:

    best: Binary string that gave the best smallest fitness

    best_eval: Fitness of best element in the population

    If best_eval = k, there is a covering of size k.
    
    '''
    # initial population of random bitstring
    # pop = [np.random.randint(0,2,n_bits).tolist() for _ in range(n_pop)]
    pop = []
    for _ in range(n_pop):

        pop_elem = np.zeros(n_bits,dtype = int)
        for i in np.random.choice(n_bits,k,replace = False):
            pop_elem[i] = 1

        pop.append(pop_elem.tolist())

   

    best, best_eval = pop[0],objective(num_edges_G,pop[0],G)

    print('Initial value f(%s) = %.3f'%(pop[0],best_eval))
    # enumerate generations
    for gen in range(n_iter):

        

        #evaluate all cadidates in the population

        scores = [objective(num_edges_G,c,G) for c in pop]    

       

        # chec for new best solution

        for i in range(n_pop):
            if scores[i]< best_eval  :
                best,best_eval = pop[i],scores[i]
                #print(">%d, new best f(%s) = %.3f"%(gen,pop[i],scores[i]))

            if best_eval == 0:

                return [best,best_eval]

        # select parents 
        selected= [selection(pop,n_pop,scores) for _ in range(n_pop)]
        children = list()

        for i in range(0,n_pop,2):
            # Select parents in pairs
            p1, p2 = selected[i], selected[i+1]
         
            # Crossover and mutation 
            for c in crossover_min_vertex_cov(p1,p2,n_cross,r_cross):
                # Mutation
               
                mutation_min_vertex_cov(c,n_bits,n_mut,r_mut,k)
                # Store for next generation
                children.append(c)
            # Replace popuation
            pop = children
    
         
    return [best,best_eval]


def genetic_algorithm_min_vertex_opt(n_bits: int , n_iter: int, n_pop: int, r_cross: float,r_mut: float,n_cross : int ,n_mut: int ,num_edges_G: int,objective, G):
    '''
    Input:

    objective: function that has two parameters num_edges_g and bitstring c

    n_bits: length of population element

    n_iter: number of iterations for the genetic algorithm

    n_pop: number of elements in the population

    r_cross: parameter to determine if a crossing occurs or not

    r_mut: parameter to determine if a mutation occurs or not

    n_cross: maximum number of entries exchanged in a cross over requirement n_cross<k

    n_mut: maximum number of entries mutated, requirement n_mut <k and n_mut<n_bits-k

    k: Decision problem, is there a vertex cover of size k?

    num_edges_g: number of edges in graph G.

    G: graph


    Output:

    best: Binary string that gave the best smallest fitness

    best_eval: Fitness of best element in the population

    If best_eval = k, there is a covering of size k.
    
    '''

    # Binary search strategy to find the minimum vertex cover 

    lb = 0

    ub = n_bits

    k = int((lb+ub)/2)

    

    while lb<ub:

        # print(lb,ub,k)        

        best,best_eval = genetic_algorithm_min_vertex_decision(n_bits,n_iter,n_pop,r_cross,r_mut,n_cross,n_mut,k,num_edges_G,cost_cover,G)

        # print(best,best_eval)

        if best_eval == 0:

            ub = k

            k = int((lb+ub)/2)

            ub -=1

        else:

            lb = k

            k = int((lb+ub)/2)

            lb += 1

        # print(lb,ub,k)
    return k,best,best_eval

