#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:29:36 2022

@author: sashabakker
"""

from math import floor
from copy import copy, deepcopy
from timeit import default_timer as timer

class Graph:
    def __init__(self, graph_file):

        self.vertex_degree = {}
        self.graph_file = graph_file
        self.edges = {}
        self.n_vertices = 0
        self.n_edges = 0
        self.vertices = []
        self.cover = [] # Our partial vertex cover

    def read_file(self):
        
        # Read all lines in file
        with open(self.graph_file) as file:
            lines = [[int(float(j)) for j in line.rstrip().split()] for line in file]
        
        # |V|, |E|, 0
        n_vertices, n_edges, w = tuple(lines.pop(0))
        
        # Keep only |V| lines
        if len(lines) > n_vertices:
            lines = [lines[i] for i in range(n_vertices)]
            
        # Store to object
        for i in range(len(lines)):
            self.edges[i+1] = lines[i]
        
        self.n_vertices = n_vertices
        self.n_edges = n_edges
        self.vertices = list(self.edges.keys())
        self.vertex_degree = self.calculate_vertex_degree(self.vertices, self.edges)
        

    def calculate_vertex_degree(self, vertices, edges):
        
        degrees = {}
        for vertex in vertices:
            degrees[vertex] = len(edges[vertex])
            
        return degrees
            
    def remove_vertex(self, vertex):
        # Vertex is in partial cover C
        # EMVC( G \ v,  min(UB,|C1|), C ∪ v )
        
        """ Remove all edges connected to vertex """
        neighbors = self.edges.pop(vertex) # list of neighboring vertices
        # Remove vertex from neighbor edges 
        for neighbor in neighbors:
            
            self.edges[neighbor].remove(vertex)
            # I checked that there is only one edge (neighbor, vertex) to remove since remove() only removes once.

            
        self.n_edges = self.compute_n_edges(self.edges)
        
        """ Remove vertex """
        self.vertices.remove(vertex)
        self.n_vertices = len(self.vertices)
        
        """ Update vertex degrees """
        self.vertex_degree = self.calculate_vertex_degree(self.vertices, self.edges)
        
        """ Add the vertex to the partial cover C """
        self.cover.append(vertex)
    
    def compute_n_edges(self, edges):
        
        edges_prime = 0 # |E'|
        for key in edges.keys():
            
            edges_prime += len(edges[key])
        
        # The count of edges is always even because the graph is undirected
        # Meaning, every edge is connected twice between two verices
        
        return edges_prime // 2

    
    def remove_neighborhood(self, vertex):
        # Vertex is not in partial cover C
        # EMVC( G \ N^*(v), UB, C ∪ N(v) )
        
        """ Remove all edges connected to vertex neighbors (including the vertex)"""
        neighbors = self.edges.pop(vertex) # list of neighboring vertices
        # We have now removed the row 'vertex'
        
        for neighbor in neighbors:
            

            # We have now removed the row 'neighbor'
            self.edges[neighbor].remove(vertex)
            # I checked that there is only one edge (neighbor, vertex) to remove since remove() only removes once.

            
            adj_vertices = self.edges.pop(neighbor)
            
            # Removing all instances of the neighbor vertices in adjacent vertices
            for adj_vertex in adj_vertices:
                
                self.edges[adj_vertex].remove(neighbor)
                # I checked that there is only one edge (neighbor, vertex) to remove since remove() only removes once.

                    
        self.n_edges = self.compute_n_edges(self.edges)
        
        """ Remove closed neighborhood from vertices and add the neighbors to the partial cover C """
        self.vertices.remove(vertex)
        for neighbor in neighbors:
            self.vertices.remove(neighbor)
            self.cover.append(neighbor)
        
        """ Update vertex degrees """
        self.vertex_degree = self.calculate_vertex_degree(self.vertices, self.edges)
    
    def degLB(self):
        
        vertices = deepcopy(self.vertices)
        edges = deepcopy(self.edges)
        vertex_degree = deepcopy(self.vertex_degree)
        n_edges = deepcopy(self.n_edges)
        
        # Keep track of degrees for vi'
        degrees = []
        
        while sum(degrees) < n_edges:

            highest_degree_vertex = max(vertex_degree, key=vertex_degree.get)
            degrees.append(vertex_degree[highest_degree_vertex])

            """ Remove all edges connected to vertex """
            neighbors = edges.pop(highest_degree_vertex)
            for neighbor in neighbors:

                edges[neighbor].remove(highest_degree_vertex)
                # I checked that there is only one edge (neighbor, vertex) to remove since remove() only removes once.
                    
            """ Remove vertex """
            vertices.remove(highest_degree_vertex)
            
            """ Update vertex degrees """
            vertex_degree = self.calculate_vertex_degree(vertices, edges)

        
        """ Satisfied condition: sum(degrees) >= n_edges """
        i = len(degrees) # i
        
        """ We must compute the degree of v'(i+1) """
        highest_degree_vertex = max(vertex_degree, key=vertex_degree.get) # This is v'(i+1)
        highest_degree = vertex_degree[highest_degree_vertex] # This is d(v'(i+1))
        
        edges_prime = self.compute_n_edges(edges) # |E'|

        # Do not want to divide by zero. If there are zero edges the highest degree must be zero as well.
        if int(edges_prime) == 0:
            frac = 0
        else:
            frac = edges_prime / highest_degree
            
        return floor( i + frac )
         
     

graph_file = "jazz.graph" #"test.txt" #"jazz.graph" #"sasha.txt" #"karate.graph"

# Read File
G = Graph(graph_file)
G.read_file()

# Initialize variables
frontier = [G]
best = (G.n_vertices, G)


while len(frontier) != 0 :
    
    G_prime = frontier.pop()

    v = max(G_prime.vertex_degree, key=G_prime.vertex_degree.get)

    states = [1, 0]
    
    for state in states:
        
        G_bar = deepcopy(G_prime)

        
        if state == 1:
            # vertex in cover
            G_bar.remove_vertex(v)
        
        elif state == 0:
            # vertex not in cover
            G_bar.remove_neighborhood(v)
        

        if G_bar.n_edges == 0:
            # found complete solution
            
            if len(G_bar.cover) < best[0]:
                best = ( len(G_bar.cover), G_bar)
    
        elif len(G_bar.cover) + G_bar.degLB() < best[0]:
            frontier.append(G_bar)
    
            
print("\n\nMVC: ", best[0])           


    
    
    


   
            
    
            
