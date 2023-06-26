import networkx as nx
from math import floor
from operator import itemgetter

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

