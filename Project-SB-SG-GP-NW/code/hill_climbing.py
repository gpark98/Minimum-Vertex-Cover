import time
import sys
import random
import networkx as nx
from networkx.algorithms.approximation import min_weighted_vertex_cover


def hill_climbing_opt(G, random_seed, max_time):
    random.seed(random_seed)

    start_time = time.time()

    # Find an initial vertex cover

    C = []
    update_times = []
    update_results = []

    H = G.copy()

    while H.size():
        max_grade = max(H.degree, key=lambda x: x[1])[1]
        max_grade_nodes_list = [node[0] for node in H.degree if node[1] == max_grade]

        n = max_grade_nodes_list[0]

        H.remove_node(n)
        C.append(n)

    C_new = C
    
    lst = list(G.edges)

    while ((time.time() - start_time) < max_time):

        c = 0
        for u,v in G.edges:
            if u not in C and v not in C:
                c = -1
        if c == 0:

            # C is a vertex cover, trace the improvements

            found_time = time.time() - start_time
            update_times.append(found_time)

            update_results.append(len(C))

            C_new = C.copy()
            C.pop(random.randrange(len(C)))
        

        if len(C) == 0:
            break
        # select exiting vertex
        
        values = [0 for _ in range(len(C))]
        dic = dict(zip(C, values))
        for u,v in G.edges:
            if u in C and v not in C:
                dic[u] += 1
            if u not in C and v in C:
                dic[v] += 1
        a = min(dic, key=dic.get)

        C.remove(a)

        # select entering vertex
        random.shuffle(lst)
        for u,v in lst:
            if u not in C and v not in C:
                C.append(v)
                break
                
    
    C_new.sort()
    
    return len(C_new), C_new, update_times, update_results