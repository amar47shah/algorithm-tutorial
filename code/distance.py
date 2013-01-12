

def distanceBF(graph, origin, destination):

    """A breadth-first algorithm for computing the distance between two vertices of a graph."""

    queue = [origin]
    distances = []
    
    try:
        for i in range(0, graph.order()):
            distances.append('infinity')
        distances[origin] = 0
    except AttributeError:
        return "Invalid graph."
    except IndexError:
        return "Invalid initial vertex: %d" % (origin)
    
    while len(queue) > 0:
        
        v = queue.pop(0)
        
        if v == destination:
            return distances[v]
        
        try:
            for w in graph.neighbors(v):
                if distances[w] == 'infinity':
                    distances[w] = distances[v] + 1
                    queue.append(w)
        except AttributeError:
            return "Invalid graph."
        except LookupError:
            return "Invalid initial vertex: %d" % (origin)
    
    try:
        return distances[destination]
    except IndexError:
        return "Invalid terminal vertex: %d" % (destination)
        


def distanceDF(graph, origin, destination):
    
    """A breadth-first algorithm for computing the distance between two vertices of a graph."""
    
    stack = [origin]
    distances = []
    
    try:
        for i in range(0, graph.order()):
            distances.append('infinity')
        distances[origin] = 0
    except AttributeError:
        return "Invalid graph."
    except IndexError:
        return "Invalid initial vertex: %d" % (origin)
    
    while len(stack) > 0:

        v = stack.pop()
        
        if v == destination:
            return distances[v]
            
        try: 
            for w in graph.neighbors(v):
                if distances[w] == 'infinity':
                    distances[w] = distances[v] + 1
                    stack.append(w)
        except AttributeError:
            return "Invalid graph."
        except LookupError:
            return "Invalid initial vertex: %d" % (origin)

    try:
        return distances[destination]
    except IndexError:
        return "Invalid terminal vertex: %d" % (destination)
