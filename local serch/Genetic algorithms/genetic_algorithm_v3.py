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

from operator import itemgetter

# Function used for greedy algorithm

def node_max_deg(G):
    '''
    Input: list of edges of an entire graph G

    Output: node with maximum degree
    
    '''

    return sorted(G.degree,key = lambda x: x[1], reverse=True)[0][0]

# Greedy algorithm for finding initial condition 

def max_deg_greedy(G):

    '''
    Input: Graph G

    Output: Greedy solution for G
    
    '''

    C = []

    GG = G.copy()

    while len(GG.edges) > 0:

        # Add the node with maximum degree

        max_node = node_max_deg(GG)

        # Remove the node from the graph GG

        GG.remove_node(max_node)

        C.append(max_node)


    return C

# Selection process of genetic algorithm

def selection(pop,n_pop,scores):

    k = int(n_pop*0.1+2)
    #Select first parent
    selection_ix = np.random.randint(n_pop)
    # Randomly pick k-1 parents
    for ix in np.random.randint(0,n_pop,k-1):

        # Compare score of parents and select best score
        if scores[ix] < scores[selection_ix]:

            selection_ix = ix

    return pop[selection_ix]

# cost/fitness function

def cost_cover(num_edges_G: int,n_vert,C: list,G):

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


    sum1 = 0

    for i in range(n_vert):
        sum2 = 0

        if C[i] == 0 :#and i+1 in list(G.nodes):
            for j in list(G.neighbors(i+1)):

                sum2 += 1-C[j-1]
        sum1 += (1-C[i])*sum2

    return sum1

def vert_min_degree(V,G,N= 1):
    '''
    Input:

    V: Dictionary of degrees

    G: graph

    N: desired largest values
    
    Output:
        
    node_max_degree: node with maximum degree

    '''

    sort = np.argsort(np.array([G.degree[x] if G.degree[x] > 0 else np.infty for x in V]))
    
    res = np.array(V)[sort]

    return res[:N].tolist()

def edges_not_covered(C,G):

    return [x  for x in G.edges if (C[x[0]-1] == 0 and C[x[1]-1] == 0) ]

def return_to_state_space(C,G,k):

    '''
    Input:

    C: binary string 

    G: graph

    k: size of decision problem

    Output:

    C: with only k 1s
    
    '''

    # If C is in a larger state space, find the sum(C)-k vertices with minimum degree and remove them
    if sum(C)> k:

        N = sum(C)-k

        V = np.where(np.asanyarray(C)==1)[0]+1

        V = V.tolist()
        # print(type(V))

        #  Find the vertices with minimum degree

        res  = vert_min_degree(V,G,N)

        # print(type(res))

        V  = V+30*res 

        for x in np.random.choice(V,N,replace= False):

            C[x-1] = 0

        return C
    
    # If sum(C)<k add k-sum(C) vertices of edges not included

    # if sum(C) < k:

    #     edges = edges_not_covered(C,G)

    #     while(sum(C)<k):

    #         new_node = edges[np.random.choice(len(edges))][np.random.choice(2)]

    #         if C[new_node-1] == 0:

    #             C[new_node-1] = 1
        
    #     return C
    
    return C



def crossover_min_vertex_cov(p1: list,p2: list,n_bits: int,r_cross: float,G,k):
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

        p = np.random.choice(n_bits)

        c1 = p1[:p]+p2[p:]

        c2 = p2[:p]+p1[p:]

        c1 = return_to_state_space(c1,G,k)

        c2 = return_to_state_space(c2,G,k)
        

    return [c1,c2]


    
def mutation_min_vertex_cov(bitstring: list,n_bits: int,n_mut: int,r_mut: float, k :int,G):
    # Given a bitstring
    # Go through each elemnt of the string
 

    if np.random.rand() < r_mut:

        # Transform the bitstring in a set of vertices

        V = np.where(np.asanyarray(bitstring)==1)[0]+1

        # Find the edges not covered

        current_edges_not_covered = edges_not_covered(bitstring,G)

        len_edges = len(current_edges_not_covered)

        len_V = len(V)

        if (len_edges>0):

            # Find the edge with minimum degree
                    
            #node_min_deg= vert_min_degree(V,G)[0] 

            

            m = max(1,np.random.choice(min(len_edges,len_V))) 

            #node_min_deg = V[np.random.choice(len(V))]

            nodes_min_deg = [V[x] for x in np.random.choice(len_V,m,replace=False)]
            # Randomlly select a vertex from an edge not included 

            # new_node = current_edges_not_covered[np.random.choice(len_edges)][np.random.choice(2)]

            new_nodes = [current_edges_not_covered[x][np.random.choice(2)]for x in np.random.choice(len_edges,m,replace=False)]
            
            for i in range(m):

                bitstring[new_nodes[i]-1] = 1
                
                bitstring[nodes_min_deg[i]-1] = 0

        

    return bitstring

# genetic algorithm
def genetic_algorithm_min_vertex_decision(n_bits: int , n_iter: int, n_pop: int, r_cross: float,r_mut: float,n_cross : int ,n_mut: int ,k: int,num_edges_G: int,objective, G,initial_element):
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
    
    
    pop = []

    # Initialize population with previous best solution 

    pop.append(initial_element)

    best, best_eval = pop[0],objective(num_edges_G,n_bits,pop[0],G)

    print('Fitness of initial condition %.3f'%(best_eval))

    # Populate
    
    for _ in range(n_pop):

        # Generate an element of the popluation

        pop_elem = np.zeros(n_bits,dtype = int)

        for i in np.random.choice(n_bits,k,replace = False):

            pop_elem[i] = 1

        # Test its fitness
        
        fit_element = objective(num_edges_G,n_bits,pop[0],G)

        if fit_element < best_eval:

            best,best_eval = pop_elem, fit_element

        if best_eval == 0:
        
            return [best,best_eval]

        pop.append(pop_elem.tolist())
    
    prev_best_eval = 0 

    # Counter for stopping criteria

    counter = 0 
    
    # enumerate generations
    for gen in range(n_iter):

        #evaluate all cadidates in the population

        scores = [objective(num_edges_G,n_bits,c,G) for c in pop]  


        # print(scores)  

        # chec for new best solution

        for i in range(n_pop):
            if scores[i]< best_eval  :
                best,best_eval = pop[i],scores[i]
                print(">%d, new best = %.3f"%(gen,scores[i]))

            if best_eval == 0:

                return [best,best_eval]

        # Count for how many iterations the solution has not improved
        if best_eval == prev_best_eval:
            counter += 1
        
        prev_best_eval = best_eval

        # If the solution does not decreases
        if counter == 550:
            print('Terminated due no decrease in best eval')
            return best,best_eval
    
        # select parents 
        selected= [selection(pop,n_pop,scores) for _ in range(n_pop)]

        children = list()

        for i in range(0,n_pop,2):
            # Select parents in pairs
            p1, p2 = selected[i], selected[i+1]
         
            # Crossover and mutation 
            for c in crossover_min_vertex_cov(p1,p2,n_bits,r_cross,G,k):
                # Mutation
               
                mutation_min_vertex_cov(c,n_bits,n_mut,r_mut,k,G)
                # Store for next generation
                children.append(c)
            # Replace popuation
            pop = children
    
         
    return [best,best_eval]


def genetic_algorithm_min_vertex_opt(n_bits: int , n_iter: int, n_pop: int, r_cross: float,r_mut: float ,num_edges_G: int, G, random_seed):
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

    np.random.seed(random_seed)

    # Find an initial vertex cover with maximum degree greedy algorithm

    initial_cover = max_deg_greedy(G) #set of vertices

    # We know that for len(initial_cover) there is a cover, try for len(initial_cover)-1

    k = len(initial_cover)-1

    # Initial cover has more elements than the current k for the decision problem. 

    # Transfrom the set of vertices into a binary string 

    initial_cover_binary = np.zeros(n_bits,dtype= int).tolist()

    for x in initial_cover:

        initial_cover_binary[x-1] = 1

    # Store current best solution
        
    current_best_eval = cost_cover(num_edges_G,n_bits,initial_cover_binary,G)

    current_best = initial_cover_binary.copy()

    # Remove the vertex with minimum degree

    node_min_deg= vert_min_degree(initial_cover,G)[0]

    initial_cover_binary[node_min_deg-1] = 0

    n_cross = int(k*np.random.rand())

    n_mut = int(k*np.random.rand())

    print('-------------------------%d-----------------'%(k))
    
    best,best_eval = genetic_algorithm_min_vertex_decision(n_bits,n_iter,n_pop,r_cross,r_mut,n_cross,n_mut,k,num_edges_G,cost_cover,G,initial_cover_binary)

    # If there's a covering for k, necessarely best_eval = 0

    while(best_eval < 1):

        current_best,current_best_eval = best,best_eval

        k -=1 

        print('-------------------------%d-----------------'%(k))

        # n_cross = int(k*np.random.rand())

        # n_mut = int(k*np.random.rand())

        # We use the previous best solution as part of our new population

        # Find vertex with minimum degree and remove it from the current solution

        V = np.where(np.asanyarray(current_best)==1)[0]+1

        node_min_deg= vert_min_degree(V,G)[0]

        current_best_remove_min_deg_vert = current_best.copy()

        current_best_remove_min_deg_vert[node_min_deg-1] = 0

        # Is there a covering of size k?

        best,best_eval = genetic_algorithm_min_vertex_decision(n_bits,n_iter,n_pop,r_cross,r_mut,n_cross,n_mut,k,num_edges_G,cost_cover,G,current_best_remove_min_deg_vert)

    print('asldfkj')
        
    
    k = sum(current_best)

    return k,current_best,current_best_eval




# def vert_max_degree(V,G,N):
#     '''
#     Input:

#     V: Dictionary of degrees

#     G: graph

#     N: desired largest values
    
#     Output:
        
#     node_max_degree: node with maximum degree

#     '''
            
#     degrees_V = [G.degree[x] for x in V]

#     dict_current_V = dict(zip(V,degrees_V))

#     degrees_V = [G.degree[x] for x in V]

#     dict_current_V = dict(zip(V,degrees_V))

#     res = list(dict(sorted(dict_current_V.items(), key = itemgetter(1),reverse= True)[:N]).keys())    

#     return res
