def distance_dijkstra(graph, origin, destination):
    
    parent = []
    queue = []
    distances = []
    
    try:
        for i in range(0, graph.order()):
            distances.append('infinity')
            queue.append(i)
        distances[origin] = 0
    except AttributeError:
        return "Invalid graph."
    except IndexError:
        return "Invalid initial vertex: %d" % (origin)
    
    while len(queue) > 0:
        
        min = 0
        for v in queue:
            if distances[v] > distances[min]:
                min = v
        queue.remove(min)
        
        for v in graph.adjacent(min):
            if v in queue:
                if distances[v]
