from timeit import default_timer as timer
from utils_BnB import update_frontier, retrieve_parent_graph, cover_size, remove_neighborhood, degLB, get_mvc, make_graph


def BnB(G, timelimit):
    """
    

    Parameters
    ----------
    G : NetworkX
        Graph for which to compute the MVC.
    timelimit : INT
        Number of seconds at which to stop the algorithm.

    Returns
    -------
    len_mvc : INT
        Length of the MVC.
    mvc : LIST
        List of nodes in the MVC.
    update_times : LIST
        List of times at which a better solution was found. 
    update_results : LIST
        List of lengths of MVC's.

    """
    
    print('G: |V| = ', G.number_of_nodes(),'\nG: |E| = ', G.number_of_edges())
    
    start_time = timer()
    C_opt = [] # Optimal vertex cover
    C_prime = [] # Partial vertex cover
    UB = G.number_of_nodes() # Upper bound
    G_prime = G.copy() # Partial graph
    frontier = update_frontier([], G_prime, 0, 0)  # Set to explore 
    deadend = False # reached dead end
    
    # Logging
    update_times = []
    update_results = []
    
    
    while len(frontier) != 0:
        
        if timer() - start_time >= timelimit:
            break
        
        if deadend == True:
            C_prime, G_prime = retrieve_parent_graph(frontier, C_prime, G_prime, G)
            deadend = False
        
        child, parent = frontier.pop() 
        node, state = child
        
        
        if state == 0: 
            # Node is not in cover
            G_prime, neighbors = remove_neighborhood(G_prime, node) 
            C_prime.extend([(neighbor, 1) for neighbor in neighbors])
        
        elif state == 1: 
            # Node is in cover
            G_prime.remove_node(node)
        
        C_prime.append((node, state))
        C_prime_size = cover_size(C_prime)
        
        if G_prime.number_of_edges() == 0:
            # Candidate Solution Found: reached end of branch
            deadend = True
            if C_prime_size < UB:
                
                found_time = timer() - start_time
                update_times.append(found_time)
                update_results.append(C_prime_size)
                print(f"|C| = {C_prime_size}, t = {round(found_time, 5)} seconds")
                
                C_opt = C_prime.copy()
                UB = C_prime_size
                   
        else:   
            # Partial Solution Found
            if C_prime_size + degLB(G_prime) < UB:
                # Partial solution is worth exploring
                frontier = update_frontier(frontier, G_prime, node, state)
            else:
                # Partial solution not worth exploring
                deadend = True

    
    print(f"Length of MVC = {UB}, t = {round(timer() - start_time, 5)} seconds")
    
    len_mvc, mvc = get_mvc(C_opt)
    
    if len_mvc == 0:
        
        mvc = list(G.nodes)
        len_mvc = len(mvc)
    
    return len_mvc, mvc, update_times, update_results

"""
graph_filename = "karate.graph" 
G = make_graph(graph_filename)
timelimit = 3600 # 1 hour
print("G: " + graph_filename)
len_mvc, mvc, update_times, update_results =  BnB(G, timelimit)

graph_name = graph_filename.split(".")[0]

# Write solution file
f = open(graph_name + "_BnB.sol","w+")
f.write(str(len_mvc) + "\n")
for i in range(len(mvc)):
    
    v = str(mvc[i])
    
    if i < len(mvc) - 1:
    
        f.write(v + ", ")
    else:
        f.write(v)
f.close()

# Write trace file
f = open(graph_name + "_BnB.trace","w+")
for i in range(len(update_times)):
    
    time = str(round(update_times[i],6))
    sol = str(update_results[i])
    
    f.write(time + ", " + sol + "\n")
f.close()
"""





