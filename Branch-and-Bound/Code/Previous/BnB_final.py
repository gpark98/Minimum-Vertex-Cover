
import networkx as nx
from math import floor
from operator import itemgetter
from timeit import default_timer as timer

def maximum_degree_node(graph):
    """
    
    
    Parameters
    ----------
    graph : NetworkX 
        Graph from which we want to identify the maximum degree node.

    Returns
    -------
    TUPLE
        D(node, degree of node)
        
    """
    
    return max(graph.degree, key = itemgetter(1))

def degLB(graph):
    """
    
    
    Parameters
    ----------
    graph : NetworkX
        Graph from which we want to compute the degree-based lower bound.

    Returns
    -------
    INT
        Degree-based lower bound.
        
    """
    
    G = graph.copy()
    degrees = []
    n_edges = G.number_of_edges() 
    
    while sum(degrees) < n_edges:
        
        node, max_deg = maximum_degree_node(G)
        degrees.append(max_deg)
        G.remove_node(node)

    i = len(degrees)
    
    node, max_deg = maximum_degree_node(G)
    edges_prime = G.number_of_edges()
    
    if int(edges_prime) == 0:
        frac = 0
    else:
        frac = edges_prime / max_deg
    
    return floor( i + frac )


def cover_size(cover):
    """
    
    
    Parameters
    ----------
    cover : LIST
        List of tuples (node, state) in cover, where state == 1 if node in cover, 0 otherwise.

    Returns
    -------
    INT
        Number of nodes in cover with state == 1.
        
    """
    
    return sum(x[1] for x in cover)


def make_graph(graph_filename):
    """
    
    
    Parameters
    ----------
    graph_filename : STRING
        Name of file that contains the graph's adjacencey list.

    Returns
    -------
    G : NetworkX
        Graph constructued from the adjacency list.

    """
    
    with open(graph_filename) as file:
        lines = [[int(float(j)) for j in line.rstrip().split()] for line in file]

    n_vertices, n_edges, w = tuple(lines.pop(0))

    if len(lines) > n_vertices:
        lines = [lines[i] for i in range(n_vertices)]

    edges_dict = {}
    for i in range(len(lines)):
        edges_dict[i+1] = lines[i]
    
    G = nx.Graph(edges_dict)
	
    return G


def retrieve_parent_graph(frontier, C_prime, G_prime, G):
    """
    

    Parameters
    ----------
    frontier : LIST
        List of tuples ((child node, child state), (parent, parent state)) to explore branches.
    C_prime : LIST
        List of tuples (node, state) in cover, where state == 1 if node in cover, 0 otherwise.
    G_prime : NetworkX
        Partial graph of G.
    G : NetworkX
        The original graph.

    Returns
    -------
    C_prime : LIST
        Updated partial cover.
    G_prime : TYPE
        Graph of parent node.

    """

    child, parent = frontier[-1] # (child node, child state) (parent node, parent state)
    
    
    if parent == (0, 0):
        # Original Graph
        
        C_prime.clear()
        G_prime = G.copy()
    
    else:
        # Graph of Parent Node
        
        number_to_remove = len(C_prime) - C_prime.index(parent) - 1
        
        for i in range(number_to_remove):
        
            node, state = C_prime.pop()
            G_prime.add_node(node)
            
            # Add previously removed nodes to graph
            C_prime_nodes = [x[0] for x in C_prime]
            
            for neighbor in list(G.neighbors(node)):
                
                if neighbor not in C_prime_nodes:
                    # Add previously removed edge to graph
                    
                    G_prime.add_edge(neighbor, node) 

    return C_prime, G_prime


def remove_neighborhood(graph, node):
    """
    

    Parameters
    ----------
    graph : NetworkX
        Graph from which to remove the neighborhood of a node.
    node : INT
        Node whose neighborhood will be removed from the graph.

    Returns
    -------
    graph : NetworkX
        Updated graph.
    neighbors : LIST
        List of neighbors of the node.

    """

    neighbors = list(graph.neighbors(node))
    graph.remove_nodes_from(neighbors)
        
    return graph, neighbors  

def update_frontier(frontier, G_prime, parent, parent_state):
    """
    

    Parameters
    ----------
    frontier : LIST
        List of tuples ((child node, child state), (parent, parent state)) to explore branches.
    G_prime : NetworkX
        Partial graph of G.
    parent : INT
        Parent node.
    parent_state : INT
        State of parent node where state == 1 if node in cover, 0 if not in cover

    Returns
    -------
    frontier : LIST
        Updated frontier.

    """
    
    v, v_deg = maximum_degree_node(G_prime)
    frontier.append(( (v, 0), (parent, parent_state)))
    frontier.append(( (v, 1), (parent, parent_state)))
    
    return frontier

def get_mvc(C_opt):
    """
    

    Parameters
    ----------
    C_opt : LIST
        List of tuples (node, state) in optimal cover, where state == 1 if node in cover, 0 otherwise.

    Returns
    -------
    INT
        Number of nodes in the minimum vertex cover
    mvc : LIST
        List of nodes in the minimum vertex cover.

    """
    
    mvc = [x[0] for x in C_opt if x[1] == 1]
    mvc.sort()
    
    return len(mvc), mvc

    


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


graph_filename = "email.graph" # 15 minutes of "power.graph" does not produce a better solution
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







