from collections import deque
import math
from disjointset import DisjointIntegerSets
from intpq import PQInts, ArrayPQInts

class Graph :
    """Graph represented with adjacency lists."""

    __slots__ = ['_adj']

    def __init__(self, v=10, edges=[]) :
        """Initializes a graph with a specified number of vertexes.

        Keyword arguments:
        v - number of vertexes
        edges - any iterable of ordered pairs indicating the edges 
        """
        self._adj = [ _AdjacencyList() for i in range(v) ]
        for u, v in edges :
            self.add_edge(u, v)
        
    def add_edge(self, a, b) :
        """Adds an edge to the graph.

        Keyword arguments:
        a - first end point
        b - second end point
        """
        self._adj[a].add(b)
        self._adj[b].add(a)

    def num_vertexes(self) :
        """Gets number of vertexes of graph."""        
        return len(self._adj)

    def degree(self, vertex) :
        """Gets degree of specified vertex.

        Keyword arguments:
        vertex - integer id of vertex
        """        
        return self._adj[vertex]._size

    def bfs(self, s) :
        """Performs a BFS of the graph from a specified starting vertex.
        Returns a list of objects, one per vertex, containing the vertex's distance
        from s in attribute d, and vertex id of its predecessor in attribute pred.

        Keyword arguments:
        s - the integer id of the starting vertex.
        """
        
        class VertexData :
            __slots__ = [ 'd', 'pred' ]

            def __init__(self) :
                self.d = math.inf
                self.pred = None

        vertexes = [VertexData() for i in range(self.num_vertexes())]
        vertexes[s].d = 0
        q = deque([s])
        while len(q) > 0 :
            u = q.popleft()
            for v in self._adj[u] :
                if vertexes[v].d == math.inf :
                    vertexes[v].d = vertexes[u].d + 1
                    vertexes[v].pred = u
                    q.append(v)
        return vertexes

    def dfs(self, on_finish=lambda v : None) :
        """Performs a DFS of the graph.  Returns a list of objects, one per vertex, containing
        the vertex's discovery time (d), finish time (f), and predecessor in the depth first forest
        produced by the search (pred).

        Keyword arguments:
        on_finish - A function with 1 argument to call each time the dfs finishes a vertex.
        """

        class VertexData :
            __slots__ = [ 'd', 'f', 'pred' ]

            def __init__(self) :
                self.d = 0
                self.pred = None

        vertexes = [VertexData() for i in range(self.num_vertexes())]
        time = 0

        def dfs_visit(u) :
            nonlocal time
            nonlocal vertexes

            time = time + 1
            vertexes[u].d = time
            for v in self._adj[u] :
                if vertexes[v].d == 0 :
                    vertexes[v].pred = u
                    dfs_visit(v)
            time = time + 1
            vertexes[u].f = time
            on_finish(u)

        for u in range(len(vertexes)) :
            if vertexes[u].d == 0 :
                dfs_visit(u)
        return vertexes

    def get_edge_list(self) :
        """Returns a list of the edges of the graph
        as a list of tuples:
        [ (a, b), (c, d), ... ] where a, b, c, d, etc are
        vertex ids.  
        """
        return [ (u,v) for u, uList in enumerate(self._adj) for v in uList if v > u]


class WeightedGraph(Graph) :
    """Weighted graph represented with adjacency lists."""

    def __init__(self, v=10, edges=[], weights=[]) :
        """Initializes a weighted graph with a specified number of vertexes.

        Keyword arguments:
        v - number of vertexes
        edges - any iterable of ordered pairs indicating the edges 
        weights - list of weights, same length as edges list
        """
        self._adj = [ _WeightedAdjacencyList() for i in range(v) ]
        for i, (u,v) in enumerate(edges) :
            self.add_edge(u, v, weights[i])
                
    def add_edge(self, a, b, w=1) :
        """Adds an edge to the graph.

        Keyword arguments:
        a - first end point
        b - second end point
        """
        self._adj[a].add(b, w)
        self._adj[b].add(a, w)

    def get_edge_list(self, with_weights=False) :
        """Returns a list of the edges of the graph
        as a list of tuples.  Default is of the form
        [ (a, b), (c, d), ... ] where a, b, c, d, etc are
        vertex ids.  If with_weights is True, the generated
        list includes the weights in the following form
        [ ((a, b), w1), ((c, d), w2), ... ] where w1, w2, etc
        are the edge weights.

        Keyword arguments:
        with_weights -- True to include weights
        """
        if not with_weights :
            return super().get_edge_list()
        else :
            return [ ((u,v),w) for u, uList in enumerate(self._adj) for v, w in uList.__iter__(True) if v > u]

    def mst_kruskal(self) :
        """Returns the set of edges in some
        minimum spanning tree (MST) of the graph,
        computed using Kruskal's algorithm.
        """
        
        A = set()
        forest = DisjointIntegerSets(self.num_vertexes())
        edges = self.get_edge_list(True)
        edges.sort(key=lambda x : x[1])
        for (u,v), w in edges :
            if forest.findset(u) != forest.findset(v) :
                A.add((u,v))
                forest.union(u,v)
        return A

    def mst_prim(self, r=0) :
        """Returns the set of edges in some
        minimum spanning tree (MST) of the graph,
        computed using Prim's algorithm.

        Keyword arguments:
        r - vertex id to designate as the root (default is 0).
        """

        parent = [ None for x in range(self.num_vertexes())]
        Q = PQInts(self.num_vertexes())
        Q.insert(r, 0)
        for u in range(self.num_vertexes()) :
            if u != r :
                Q.insert(u, math.inf)
        while not Q.is_empty() :
            u = Q.extract_min()
            for v, w in self._adj[u].__iter__(True) :
                if Q.contains(v) and w < Q.get_priority(v) :
                    parent[v] = u
                    Q.change_priority(v, w)
        return { (u,v) for v, u in enumerate(parent) if u != None}

    def dijkstra_binheap(self, s):
        """Dijkstra's Algorithm using a binary heap as the PQ.

        Keyword Arguments:
        s - The source vertex.
        """
        # Programming Assignment 3:
        #   This method has been implemented for you, which
        #   simply calls the _dijkstra method that you will
        #   be implementing below, passing it a binary heap
        #   for its priority queue.
        return self._dijkstra(s, PQInts(self.num_vertexes()))

    def dijkstra_array(self, s):
        """Dijkstra's Algorithm using a simple array as the PQ.

        Keyword Arguments:
        s - The source vertex.
        """
        # Programming Assignment 3:
        #   This method has been implemented for you, which
        #   simply calls the _dijkstra method that you will
        #   be implementing below, passing it a priority queue
        #   implemented with a simple array for its priority queue.
        return self._dijkstra(s, ArrayPQInts(self.num_vertexes()))

    def _dijkstra(self, s, pq) :
        """Dijkstra's Algorithm using a priority queue
        provided as a parameter.

        Keyword Arguments:
        s - The source vertex.
        pq - The priority queue to use.
        """

        # Programming Assignment 3:
        # 1) Implement Dijkstra's Algorithm. This method has been named
        #    beginning with an _ because it is a private helper method.
        #    You'll notice two other methods earlier that call it. As you
        #    implement this method, you will need a priority queue. The
        #    priority queue that you should use is the one that will be
        #    passed to it via the parameter pq. Thus, you do not need to
        #    construct a priority queue. It is initialized for you to the
        #    correct number of vertexes in the graph.
        #
        #    Regardless of what class that priority queue object is, it has
        #    the following methods:
        #      pq.size() returns the number of elements it contains.
        #      pq.is_empty() returns either True or False indicating it if it empty.
        #      pq.insert(element, priority) inserts a new element with a given priority
        #         provided the element isn't already in the priority queue. It returns
        #         True if it added the element and False if it already contained the
        #         element.
        #      pq.peek_min() returns the element that has the lowest priority value.
        #         Its behavior is undefined if the priority queue is empty.
        #      pq.extract_min() removes and returns the element with the lowest
        #         priority value. Its behavior is undefined if the priority queue is
        #         empty.
        #      pq.contains(element) returns True if and only if the priority queue
        #         contains the element.
        #      pq.get_priority(element) returns the current priority of the element
        #         if it is in the priority queue. Its behavior is undefined if the
        #         priority queue is empty.
        #      pq.change_priority(element, priority) changes the priority of an element
        #         if it is in the priority queue, and does nothing if the element is
        #         not in the priority queue.
        #
        #    You can see examples of usage of the priority queue in the implementation
        #    of Prim's algorithm earlier in this file. Note that the Prim implementation
        #    constructs a priority queue with the PQInts initializer, which you do not
        #    need to do since that is passed to this method as the pq parameter.
        #
        #    Have this method return a list of 3-tuples, one for each vertex, such that
        #    first position is vertex id, second is distance from source vertex (i.e., what
        #    pseudocode from textbook refers to as v.d), and third is the vertex's parent
        #    (what the textbook refers to as v.pi). E.g., (2, 10, 5) would mean the shortest
        #    path from s to 2 has weight 10, and vertex 2's parent is vertex 5.
        #
        #    The parameter s is the source vertex.
        #
        #    Whenever you need to change the value of d for a vertex, don't forget to also
        #    call the appropriate method of pq to decrease that vertex's priority.  Your
        #    implementation will be incorrect if you forget to update priorities.
        pass


class Digraph(Graph) :
    """Digraph represented with adjacency lists."""

    __slots__ = [ '_indegree' ]

    def __init__(self, v=10, edges=[]) :
        self._indegree = [ 0 for i in range(v) ]
        self._adj = [ _AdjacencyList() for i in range(v) ]
        for u, v in edges :
            self.add_edge(u, v)
        
    def add_edge(self, a, b) :
        """Adds a directed edge to the graph.

        Keyword arguments:
        a - source (starting) vertex
        b - target (ending) vertex
        """
        self._adj[a].add(b)
        self._indegree[b] += 1

    def out_degree(self, vertex) :
        """Gets the outdegree of a vertex

        Keyword arguments:
        vertex - the vertex id"""
        return super().degree(vertex)

    def in_degree(self, vertex) :
        """Gets the indegree of a vertex

        Keyword arguments:
        vertex - the vertex id"""
        return self._indegree[vertex]

    def degree(self, vertex) :
        """Gets the indegree of a vertex

        Keyword arguments:
        vertex - the vertex id"""
        return self.out_degree(vertex) + self.in_degree(vertex)

    def get_edge_list(self) :
        """Returns a list of the edges of the graph
        as a list of tuples:
        [ (a, b), (c, d), ... ] where a, b, c, d, etc are
        vertex ids.  
        """
        return [ (u,v) for u, uList in enumerate(self._adj) for v in uList]

    def transpose(self) :
        """Generates and returns the transpose of this Digraph."""
        T = Digraph(self.num_vertexes())
        for u, adjacent in enumerate(self._adj) :
            for v in adjacent :
                T.add_edge(v, u)
        return T

    def topological_sort(self) :
        """Topological Sort of the directed graph (Section 22.4 from textbook).
        Returns the topological sort as a list of vertex indices.
        """
        top_sort = []
        def on_finish(u) :
            nonlocal top_sort
            top_sort.append(u)
        self.dfs(on_finish)
        top_sort.reverse()
        return top_sort

    def scc(self) :
        """Computes the strongly connected components of a digraph.
        Returns a list of sets, containing one set for each
        strongly connected component,
        which is simply a set of the vertexes in that component."""
        ordered = self.topological_sort()
        T = self.transpose()
        
        discovered = [ False for i in range(T.num_vertexes())]
        def dfs_visit(u, component) :
            nonlocal discovered
            nonlocal T

            discovered[u] = True
            component.add(u)
            for v in T._adj[u] :
                if not discovered[v] :
                    dfs_visit(v, component)

        SCC = []
        for u in ordered :
            if not discovered[u] :
                component = set()
                dfs_visit(u, component)
                SCC.append(component)
        return SCC
        

class WeightedDigraph(WeightedGraph,Digraph) :
    """Weighted Digraph represented with adjacency lists."""

    def __init__(self, v=10, edges=[], weights=[]) :
        """Initializes a weighted digraph with a specified number of vertexes.

        Keyword arguments:
        v - number of vertexes
        edges - any iterable of ordered pairs indicating the edges 
        weights - list of weights, same length as edges list
        """
        self._adj = [ _WeightedAdjacencyList() for i in range(v) ]
        for i, (u,v) in enumerate(edges) :
            self.add_edge(u, v, weights[i])
        
    def add_edge(self, a, b, w=1) :
        """Adds an edge to the graph.

        Keyword arguments:
        a - source (starting) vertex
        b - target (ending) vertex
        """
        self._adj[a].add(b, w)

    def degree(self, vertex) :
        return Digraph.degree(self, vertex)

    def get_edge_list(self, with_weights=False) :
        """Returns a list of the edges of the graph
        as a list of tuples.  Default is of the form
        [ (a, b), (c, d), ... ] where a, b, c, d, etc are
        vertex ids.  If with_weights is True, the generated
        list includes the weights in the following form
        [ ((a, b), w1), ((c, d), w2), ... ] where w1, w2, etc
        are the edge weights.

        Keyword arguments:
        with_weights -- True to include weights
        """
        if not with_weights :
            return super().get_edge_list()
        else :
            return [ ((u,v),w) for u, uList in enumerate(self._adj) for v, w in uList.__iter__(True)]
     
    def transpose(self) :
        """Generates and returns the transpose of this Digraph."""
        T = WeightedDigraph(self.num_vertexes())
        for u, adjacent in enumerate(self._adj) :
            for v, w in adjacent.__iter__(True) :
                T.add_edge(v, u, w)
        return T


class _AdjacencyList :

    __slots__ = [ '_first', '_last', '_size']

    def __init__(self) :
        self._first = self._last = None
        self._size = 0

    def add(self, vertex) :
        self._add(_AdjListNode(vertex))
        
    def _add(self, listNode) :
        if self._first == None :
            self._first = self._last = listNode
        else :
            self._last._next = listNode
            self._last = self._last._next
        self._size += 1

    def __iter__(self):
        return _AdjListIter(self)    

class _WeightedAdjacencyList(_AdjacencyList) :

    __slots__ = []

    def __init__(self) :
        super().__init__()

    def add(self, vertex, w=1) :
        self._add(_WeightedAdjListNode(vertex, w))

    def __iter__(self, weighted=False):
        if weighted :
            return _AdjListIterWithWeights(self)
        else :
            return _AdjListIter(self)    
    
class _AdjListNode :

    __slots__ = [ '_next', '_targetVertex' ]

    def __init__(self, vertex) :
        self._next = None
        self._targetVertex = vertex

class _WeightedAdjListNode(_AdjListNode) :

    __slots__ = [ '_w' ]

    def __init__(self, vertex, w=1) :
        super().__init__(vertex)
        self._w = w

class _AdjListIter :

    __slots__ = [ '_next' ]

    def __init__(self, adjlist) :
        self._next = adjlist._first
        
    def __iter__(self) :
        return self

    def __next__(self) :
        if self._next == None :
            raise StopIteration
        vertex = self._next._targetVertex
        self._next = self._next._next
        return vertex

class _AdjListIterWithWeights(_AdjListIter) :

    __slots__ = []

    def __init__(self, adjlist) :
        super().__init__(adjlist)

    def __next__(self) :
        if self._next == None :
            raise StopIteration
        vertex = self._next._targetVertex
        w = self._next._w
        self._next = self._next._next
        return vertex, w




    
