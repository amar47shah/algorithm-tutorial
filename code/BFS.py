# Python graph BFS, using Sage
#
# A breadth-first search on an undirected graph.

from sage.all import *

def breadth_first_tree(G, s):

    queue = [s]
    distances = ['inf'] * G.order()
    distances[s] = 0
    tree = []
    
    while len(queue) > 0:
        
        v = queue.pop(0)
        for w in G.neighbors(v):
            if distances[w] == 'inf':
                distances[w] = distances[v] + 1
                queue.append(w)
                tree.push[(v, w)]
    
    return (distances, tree)
    
G = graphs.FranklinGraph()
print breadth_first_tree(G)   
