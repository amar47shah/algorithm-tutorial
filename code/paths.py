def pathBF(graph, origin, destination):

    """A breadth-first algorithm for tracing a path between two vertices of a graph."""

    queue = [origin]
    path_to = []
    
    try:
        for i in range(0, graph.order()):
            path_to.append([])
        path_to[origin].append(origin)
    except AttributeError:
        return "Invalid graph."
    except IndexError:
        return "Invalid initial vertex: %d." % origin
    
    while len(queue) > 0:
        
        v = queue.pop(0)
        
        if v == destination:
            return path_to[v]
        
        try:
            for w in graph.neighbors(v):
                if path_to[w] == []:
                    path_to[w] = path_to[v][:]
                    path_to[w].append(w)
                    queue.append(w)
        except AttributeError:
            return "Invalid graph."
        except LookupError:
            return "Invalid inital vertex: %d." % origin
    
    try:
        if path_to[destination] == []:
            return "No path exists between %d and %d." % (origin, destination)
    except IndexError:
        return "Invalid terminal vertex: %d." % destination

def pathDF(graph, origin, destination):

    """A depth-first algorithm for tracing a path between two vertices of a graph."""

    stack = [origin]
    path_to = []
    
    try:
        for i in range(0, graph.order()):
            path_to.append([])
        path_to[origin].append(origin)
    except AttributeError:
        return "Invalid graph."
    except IndexError:
        return "Invalid initial vertex: %d." % origin
    
    while len(stack) > 0:
        
        v = stack.pop()
        
        if v == destination:
            return path_to[v]
        
        try:
            for w in graph.neighbors(v):
                if path_to[w] == []:
                    path_to[w] = path_to[v][:]
                    path_to[w].append(w)
                    stack.append(w)
        except AttributeError:
            return "Invalid graph."
        except LookupError:
            return "Invalid inital vertex: %d." % origin
    
    try:
        if path_to[destination] == []:
            return "No path exists between %d and %d." % (origin, destination)
    except IndexError:
        return "Invalid terminal vertex: %d." % destination
