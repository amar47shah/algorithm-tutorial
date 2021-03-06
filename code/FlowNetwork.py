"""
This code is taken from 
Joyner, Nguyen, and Cohen
Algorithmic Graph Theory
Version 0.7-r1984
2012 March 17
"""

class Edge:
    """
    The members of Edge are accessed as public.
    """
    def __init__ (self, U, V, w):
        self.source = U
        self.to = V
        self.capacity = w

    def __repr__ (self):
        return str(self.source) + " ->" + str(self.to) + " : " + str(self.capacity)

class FlowNetwork (object):
    """
    This is a graph structure with edge capacities .
    EXAMPLES :
        g = FlowNetwork()
        map(g.add_vertex, ['s', 'o', 'p', 'q', 'r', 't'])
        g.add_edge('s', 'o', 3)
        g.add_edge('s', 'p', 3)
        g.add_edge('o', 'p', 2)
        g.add_edge('o', 'q', 3)
        g.add_edge('p', 'r', 2)
        g.add_edge('r', 't', 3)
        g.add_edge('q', 'r', 4)
        g.add_edge('q', 't', 2)
        print g.max_flow('s','t')
    """

    def __init__ (self):
        self.adj, self.flow = {}, {}
        
    def add_vertex (self, vertex):
        self.adj[vertex] = []
    
    def get_edges (self, v):
        return self.adj[v]

    def add_edge (self, u, v, w=0):
        assert( u != v )
        edge = Edge(u, v, w)
        redge = Edge(v, u, 0)
        # nasty encapsulation violation
        edge.redge = redge 
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = self.flow[redge] = 0

    def find_path (self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge, residual) in path:
                result = self.find_path(edge.to, sink, path + [(edge, residual)])
                if result != None:
                    return result
                    
    def max_flow (self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            flow = min(res for edge, res in path)
            for edge, res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum (self.flow[edge] for edge in self.get_edges(source))

    def push_relabel(self, source, sink):
        pass



g = FlowNetwork()
map(g.add_vertex, ['s', 'o', 'p', 'q', 'r', 't'])
map(g.add_edge, ['s', 's', 'o', 'o', 'p', 'r', 'q', 'q'],  
                ['o', 'p', 'p', 'q', 'r', 't', 'r', 't'],
                [ 3 ,  3 ,  2 ,  3 ,  2 ,  3 ,  4 ,  2 ])
print g.max_flow('s','t')
