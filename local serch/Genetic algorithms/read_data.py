'''
Function for reading data

'''

import networkx as nwx

def read_data_graph(name_file):

    file = open(name_file)

    G = nwx.Graph()

    n_vertex,n_edges,und = [int(x) for x in file.readline().split()]

    vertex = 1

    for x in file:

        [ G.add_edge(vertex,int(y)) for y in x.split()]

        vertex +=1

    # print(G.edges)
    return n_vertex,n_edges,G

