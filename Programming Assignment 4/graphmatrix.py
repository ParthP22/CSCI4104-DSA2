import math
import sys


# Student Name: Parth Patel
#
# Programming Assignment 4
#
# Do not delete this comment containing the assignment instructions.
#
# What to Submit: Submit the following files once you complete
# the assignment:
# (a) This file: graphmatrix.py
# (b) If you do the extra credit part, then please include a
#     a specific highway graph that you used when you tested your
#     implementation (the actual highway graph file). They sometimes
#     update the data in those files, so I want to make sure I
#     have exactly what you tested with.
#
# A few notes before you begin:
#
# - As in previous assignments, you are not allowed to change the
#   names of files, classes, methods, parameters, etc. If you are wondering
#   why I have this requirement, it is because you will often find
#   yourself (such as in future jobs) tasked with implementing an
#   interface designed by someone else.  For example, in a large project,
#   smaller groups may be tasked with developing smaller parts of a
#   much larger system after the interface has been defined.  If you
#   change part of the interface without consulting the team as a
#   whole, you will break the entire system.  It is also common in
#   test-driven development for a different team to implement the
#   test cases in code from the interface alone.
#   In homework assignments, if you change the interface that I provided
#   (i.e., names of classes, methods, parameters, etc), then the
#   larger system you are breaking is the system comprised of your
#   algorithm implementations along with my test cases that I use when
#   grading.  If I have to either modify your code or my test cases
#   when grading your assignment, then you lose significant points.
#
# - You are also not allowed to change the names of any attributes
#   that I provided, which in this case is simply _W, although in your
#   code you will need to remember to use the self reference to
#   access it, such as with self._W
#
# - Also, as in the previous assignments, don't delete the docstrings
#   (the multiline strings at the start of functions and methods).
#
# Do the following:
#
# 1) Implement the initializer in the WeightedAdjacencyMatrix class,
#    which should create a matrix (i.e., Python list of Python lists) with
#    number of rows and columns both equal to size (i.e., number of vertexes).
#    Carefully read the docstring that I have for the __init__ which explains
#    the parameters.  If edges and weights are empty lists, then the
#    graph should initially have no edges.  Otherwise, initialize it
#    with the edges and weights indicated by those lists.
#    Once the __init__ is complete, the diagonal of the matrix should have
#    all 0s.  For each edge in the edge list, with corresponding weight
#    from the weights list, you should have the weight in 2 positions in
#    the matrix (remember for an undirected graph, the matrix is
#    symmetric).  For all non-edges (other than the diagonal) you must
#    have infinity, which is math.inf in Python (make sure you add the
#    import you need for that at the top).
#
#    Use the attribute I provided in __slots__ for your matrix _W (see
#    comment above). Remember to use self when referencing an object
#    attribute (i.e., self._W). Although in Java, you can often omit
#    Java's "this", in Python you cannot omit self.
#
#    You can delete the pass statement I have in there.  It is just a
#    placeholder until you have implemented this.
#
#    Read the instructions for step 2 before doing step 1.  You will find
#    it useful to have your __init__ call your add_edge implemented in
#    step 2, which will make step 3 of the assignment much easier.
#
#    Hint 1: Have your __init__ start by initializing a 2D list
#            of the appropriate size, with 0s on the diagonal and
#            infinity everywhere else.  And then have it iterate
#            over the edges calling add_edge for each edge, weight pair.
#            This will make doing step 3, with the inheritance as easy
#            as overriding add_edge, without need to override __init__
#
# 2) Implement the add_edge method of the WeightedAdjacencyMatrix class,
#    as specified in its docstring.
#    It is an undirected edge, so you'll need to set two different cells
#    of the matrix (for an undirected graph, the matrix is symmetric
#    as mentioned above).
#
#    You can delete the pass statement I have in there.  It is just a
#    placeholder until you have implemented this.
#
# 3) Override add_edge in the WeightedDirectedAdjacencyMatrix class
#    according to the docstring I've inserted in that method below.
#    Also either ensure that the __init__ from step 1 will work as is
#    in the case of a directed graph, or override it in the
#    WeightedDirectedAdjacencyMatrix so that it correctly handles the
#    directed edge case.  If you followed Hint 1 above, then you will NOT
#    need to override __init__.  And following Hint 1 is the easiest way
#    to get this to work correctly.
#
#    You can delete the pass statement I have in there.  It is just a
#    placeholder until you have implemented this.
#
#    Hint 3: Although defined in the parent class, you are able to directly
#            access _W with self._W in the WeightedDirectedAdjacencyMatrix
#            class since nothing is truly private in Python.
#
# 4) Implement the floyd_warshall method in the WeightedAdjacencyMatrix class.
#    Since it is in the parent class, you'll be able to use it with either
#    undirected or directed graphs.  Read the docstring for details of what to
#    implement.
#
#    Your method MUST NOT change self._W. So make sure when you initialize
#    D, that you make a copy of self._W.  Do NOT do: D = self._W.  That
#    doesn't copy the list, it just assigns an additional reference to it.
#    So, changing D would change self._W.  Also, do NOT do: D = self._W[:].
#    That only does a shallow copy.  Since _W is a 2D list, that will only
#    copy the first dimension.  The first dimension contains references
#    to 1D list objects, so although D will be a different list than _W,
#    D[i] will be a reference to the same list object as self._W[i],
#    so changing D[i][j] will change self._W[i][j].  You need to do a
#    deep copy. To get this correct, you will either need to write a loop
#    that does a slice on each row to copy the rows one at a time. Or
#    try importing Python's copy module, and take a look at the documentation
#    of the functions in the copy module. One of them will do the deep copy
#    that you need.
#
# 5) Implement the function test_floyd_warshall to test your implementation.
#    Your test should construct a WeightedAdjacencyMatrix object, call the
#    floyd_warshall method to compute all pairs shortest paths, and then
#    output the result with print statements.  Make sure you use a case
#    that you know the correct solution, such as a small graph where you
#    compute the solution by hand (perhaps the problem from the problem set)
#    or an example from the textbook might be good since you know the correct
#    solution to that from the book. You can just call the function from the
#    shell. You don't need to call it from an if main block. The if main
#    block is for something else for extra credit. See #6 below.
#
# 6) EXTRA CREDIT: Implement the parse_highway_graph_matrix function, and the
#    pair_shortest_path function, and the if main block at the bottom according
#    to the docstrings and comments I have there indicating what these should
#    do. The extra credit portion is worth up to 25 points.

class WeightedAdjacencyMatrix :
    """A weighted graph represented as a matrix."""

    __slots__ = ['_W']

    def __init__(self, size, edges=[], weights=[]) :
        """Initializes a weighted adjacency matrix for a graph with size nodes.

        Graph is initialized with size nodes and a specified set of
        edges and edge weights.
        
        Keyword arguments:
        size -- Number of nodes of the graph.
        edges -- a list of ordered pairs (2-tuples) indicating the
                 edges of the graph.  The default value is an empty list
                 which means no edges by default.
        weights -- a list of weights for the edges, which should be the same
                   length as the edges list.  The position of a value in
                   the weights list corresponds to the edge in the same
                   position of the edges list.
        """

        # Here I initialize the adjacency matrix to be infinity for all weights, since
        # the edges and weights list could be empty
        self._W = [[math.inf for col in range(size)] for row in range(size)]

        # Here I make the main diagonal of the adjacency matrix all zeros
        for i in range(size):
            self._W[i][i] = 0

        # Here I traverse the edges and weights lists and populate
        # the weighted adjacency matrix with its edges and weights
        for i, (u,v) in enumerate(edges):
            v1, v2 = (u,v)
            self.add_edge(v1,v2,weights[i])

        pass # replace this pass statement with the code needed to implement this



    def add_edge(self, u, v, weight) :
        """Adds an undirected edge between u to v with the specified weight.

        Keyword arguments:
        u -- vertex id (0-based index)
        v -- vertex id (0-based index)
        weight -- edge weight
        """

        # Since this method is for an undirected weighted adjacency
        # matrix, this means that the weights are the same for a pair
        # of vertices, regardless of which vertex you start with
        self._W[u][v] = weight
        self._W[v][u] = weight

        pass # replace this pass statement with the code needed to implement this

    def floyd_warshall(self) :
        """Floyd Warshall algorithm for all pairs shortest paths.

        Returns a matrix D consisting of the weights of the shortest
        paths between all pairs of vertices, and a matrix P for
        the predecessors matrix (what the textbook called PI).
        This method MUST NOT change the weight matrix of the graph
        itself.  
        """
        # Your return statement will look something like this one
        # in the comment on the following line.  That returns
        # the two matrices, with the D matrix first.  The return None
        # is just a placeholder so that this is valid Python syntax before
        # you've completed the assignment.  This comment line is
        # more like what it should look like:
        # return D, P

        # Here I initialize D as a deep copy of the original weighted adjacency matrix
        D = [[self._W[row][col] for col in range(len(self._W))] for row in range(len(self._W))]

        # Here I initialize P as a matrix with "None" for all the pi-values
        P = [[None for col in range(len(self._W))] for row in range(len(self._W))]

        # I populate the P matrix with its initial values
        for i in range(len(self._W)):
            for j in range(len(self._W)):
                if i != j and self._W[i][j] < math.inf:
                    P[i][j] = i

        # I run the main for-loops of Floyd-Warshall's algorithm
        # to find all-pairs-shortest-paths and update the D and P
        # matrices accordingly with each iteration
        for k in range(len(self._W)):
            for i in range(len(self._W)):
                for j in range(len(self._W)):
                    if D[i][k]+D[k][j] < D[i][j]:
                        D[i][j] = D[i][k]+D[k][j]
                        P[i][j] = P[k][j]

        # Here I return the D and P matrices to the user
        return D, P

class WeightedDirectedAdjacencyMatrix(WeightedAdjacencyMatrix) :
    """A weighted digraph represented as a matrix."""

    def add_edge(self, u, v, weight) :
        """Adds a directed edge from u to v with the specified weight.

        Keyword arguments:
        u -- source vertex id (0-based index)
        v -- target vertex id (0-based index)
        weight -- edge weight
        """

        # Since this method is for a directed weighted adjacency
        # matrix, it does indeed matter which vertex you start from,
        # since the direction matters
        self._W[u][v] = weight

        pass # replace this pass statement with the code needed to implement this


    

def test_floyd_warshall() :
    """See assignment instructions at top."""

    # I am showing that the initialization and other functions still work even if the graph does
    # not have edges nor weights
    print("The following is for a weighted directed graph that DOES NOT have any edges nor weights")
    # I create empty lists for edges and weights in order to test that it
    # works even if no edges have been added yet
    edges = []
    weights = []

    weighted_directed_graph = WeightedDirectedAdjacencyMatrix(5,edges,weights)

    # I run Floyd-Warshall's algorithm on the graph from above
    D, P = weighted_directed_graph.floyd_warshall()

    margin = 6

    # I print out the original weighted directed adjacency matrix
    print("The original WeightedDirectedAdjacencyMatrix: ")
    for i in range(len(weighted_directed_graph._W)):
        for j in range(len(weighted_directed_graph._W)):
            print(f"{weighted_directed_graph._W[i][j] :< {margin}}", end="    ")
        print("")
    print("")

    # I print out the completed P matrix
    print("The completed P matrix AFTER Floyd-Warshall was performed")
    for i in range(len(P)):
        for j in range(len(P)):
            print(f"{str(P[i][j]):<{margin}}", end="    ")
        print("")
    print("")

    # I print out the completed D matrix
    print("The completed D matrix AFTER Floyd-Warshall was performed")
    for i in range(len(D)):
        for j in range(len(D)):
            print(f"{D[i][j] :< {margin}}", end="    ")
        print("")



    print("\nThe following is for a weighted directed graph that DOES have edges and weights")
    print("The example I am using is from Figure 23.4 from page 658 of the textbook")

    # I create an edge-list based on the weighted adjacency matrix
    # called D0 in Figure 23.4 on page 658 of the textbook.
    # Note: each vertex ID here is one less than the vertex ID's
    # that are used in the textbook, since the textbook pseudocode
    # will start indices from 1, whereas Python starts from 0
    edges = [(0,1),(0,2),(0,4),(1,3),(1,4),(2,1),(3,0),(3,2),(4,3)]

    # These are the corresponding weights of each edge from Figure 23.4
    weights = [3,8,-4,1,7,4,2,-5,6]

    # I initialize a WeightedDirectedAdjacencyMatrix using the edge-lists and
    # edge-weights.
    # I know in the instructions you said to use a WeightedAdjacencyMatrix,
    # but I use a WeightedDirectedAdjacencyMatrix here, since I know the answer
    # to it from the textbook. 
    weighted_directed_graph = WeightedDirectedAdjacencyMatrix(5,edges,weights)

    # I run Floyd-Warshall's algorithm on the graph from above
    D, P = weighted_directed_graph.floyd_warshall()

    margin = 6

    # I print out the original weighted directed adjacency matrix
    # Note: I do understand that I should not be accessing _W outside the
    # class, since it's supposed to be private, but I'm only choosing to
    # print it here, not modify it
    print("The original WeightedDirectedAdjacencyMatrix: ")
    for i in range(len(weighted_directed_graph._W)):
        for j in range(len(weighted_directed_graph._W)):
            print(f"{weighted_directed_graph._W[i][j] :< {margin}}", end="    ")
        print("")
    print("")

    # I print out the completed P matrix
    # Note: each vertex ID here is one less than the vertex ID's
    # that are used in the textbook, since the textbook pseudocode
    # will start indices from 1, whereas Python starts from 0
    print("The completed P matrix AFTER Floyd-Warshall was performed")
    print("Note: each vertex ID is one less than the textbook, since Python")
    print("starts indices from 0, not 1")
    for i in range(len(P)):
        for j in range(len(P)):
            print(f"{str(P[i][j]):<{margin}}", end="    ")
        print("")
    print("")

    # I print out the completed D matrix
    print("The completed D matrix AFTER Floyd-Warshall was performed")
    for i in range(len(D)):
        for j in range(len(D)):
            print(f"{D[i][j] :< {margin}}", end="    ")
        print("")



    pass # replace this pass statement with the code needed to implement this

def parse_highway_graph_matrix(filename) :
    """EXTRA CREDIT: Rewrite your highway graph parser from
    assignment 2 here in this function but return a WeightedAdjacencyMatrix
    object from this function. If you had that assignment working,
    then this part of the extra credit should be very easy (i.e.,
    copying and pasting code and then making very minor adjustments
    to use construct and return a WeightedAdjacencyMatrix object
    instead of the other graph type you already have.

    Keyword arguments:
    filename - the name of a highhway graph file.
    """

    # Update from Programming Assignment 4: All the comments
    # below are from Programming Assignment 2, except for the
    # very last one. I copy and pasted this function from
    # Programming Assignment 2, and the only changes I made were
    # in the return statement so that it could be compatible
    # with the weighted adjacency matrix. I also returned the
    # number of vertices in order to do some error handling later
    # in the if-main block


    # Here we initialize the lists for vertices, edges and weights.
    # I am not sure if the naming convention is correct.
    __vertices__ = []
    __edges__ = []
    __weights__ = []

    with open(filename) as file:

        # This is to skip the first line of the file, since it's
        # just a header
        file.readline()

        # This is to acquire the number of vertices and edges
        # which is stated in the second line of the file
        num_vertices, num_edges = file.readline().split()

        # This for-loop is used to put all of the vertices in the list
        for i in range(int(num_vertices)):
            line = file.readline().split(" ")
            __vertices__.append((float(line[1]), float(line[2])))

        # This for-loop is used to put all of the edges in the list
        for i in range(int(num_edges)):
            line = file.readline().split(" ")
            __edges__.append((int(line[0]), int(line[1])))
    # with-block ends here

    # This for-loop is used to calculate the weights using the haversine function
    # and then put the weights in the list
    for (u, v) in __edges__:
        v1, v2 = (u, v)
        lat1, lng1 = __vertices__[v1]
        lat2, lng2 = __vertices__[v2]
        weight = haversine(lat1, lng1, lat2, lng2)
        __weights__.append(weight)

    # I return the WeightedGraph that is created from the information from the file.
    # I am also returning num_vertices, so it can be used to handle any out of bounds
    # errors in the if-main block.
    return WeightedAdjacencyMatrix(int(num_vertices), __edges__, __weights__), int(num_vertices)


def haversine(lat1, lng1, lat2, lng2):
    """Computes haversine distance between two points in latitude, longitude.

    Keyword Arguments:
    lat1 -- latitude of point 1
    lng1 -- longitude of point 1
    lat2 -- latitude of point 2
    lng2 -- longitude of point 2

    Returns haversine distance in meters.
    """

    # Update for Programming Assignment 4: All the comments below are
    # from Programming Assignment 2. I simply copy and pasted my haversine
    # function from there.


    # I know the instructions said not to use the special symbols,
    # so I just decided to spell them out by name so it's easier for me
    # to check against the actual formula

    R = 6371000  # in meters
    phi_1 = lat1 * math.pi / 180  # to radians
    phi_2 = lat2 * math.pi / 180  # to radians
    delta_phi = (lat2 - lat1) * math.pi / 180  # to radians
    delta_lambda = (lng2 - lng1) * math.pi / 180  # to radians

    a = math.sin(delta_phi / 2) * math.sin(delta_phi / 2) + math.cos(phi_1) * math.cos(phi_2) * math.sin(
        delta_lambda / 2) * math.sin(delta_lambda / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c

    return d  # Obviously replace this return statement with what is needed.


def pair_shortest_path(D, P, s, t) :
    """EXTRA CREDIT: This function takes D and P matrices (i.e., what is generated
    by floyd_warshall), and a source vertex (where you want to start) and
    destination or target vertex t (where you want to end up) and
    returns a pair: w, path, such that w is the weight of the shortest
    path from s to t (just a simple lookup in the D matrix) and
    path is a Python list of vertex ids starting at s and ending at t
    derived from the P matrix. If no path exists from s to t, then returns
    math.inf for w (which is what D[s][t] should be in that case), and an
    empty list for the path.

    Keyword arguments:
    D - the D matrix
    P - the Pi matrix
    s - the source vertex
    t - the destination vertex
    """

    # This if-statement checks if a path doesn't
    # exist from s to t
    if D[s][t] == math.inf:
        return D[s][t], []

    # This is where we will start checking the path from,
    # since we will work backward
    curr_vertex = t

    # This list will store the vertices in order for the
    # shortest path
    path = []

    # This while-loop will traverse the path in reverse, so
    # it will insert each vertex ID to the beginning of the path
    # in order to get the correct order
    while curr_vertex != s and P[s][curr_vertex] != None:
        path.insert(0,curr_vertex)
        curr_vertex = P[s][curr_vertex]
    # Lastly, we add the source vertex to the beginning
    path.insert(0,s)

    # The weight and the path are returned to the user
    return D[s][t], path

    # Your actual return will look something like this:
    # return w, path
    # return None # temporary until you implement this

if __name__ == "__main__" :
    # EXTRA CREDIT: Write code here that:
    #   (a) Gets the name of a highway graph file from the command line
    #       arguments.
    #   (b) Uses parse_highway_graph_matrix from above to parse that file
    #       into a WeightedAdjacencyMatrix object.
    #   (c) Runs the floyd_warshall method on that graph.
    #   (d) Then, prompts the user (use the Python docs to figure out
    #       how to do this) for a source and target vertex, s and t.
    #   (e) Uses pair_shortest_path to get the weight of the shortest
    #       path between their chosen s and t, and the path itself.
    #   (f) Outputs the weight and path.
    #   (g) Repeats d, e, and f in a loop until the user indicates they
    #       want to quit.  You can decide how to get that decision from them.

    # This function was called for testing purposes.
    # Note to Professor: In Step 5 of the directions, you said that I do not
    # need to call this function in the if-main block, which is why I commented
    # it out.
    # test_floyd_warshall()

    # This if-statement tests to see if an argument has been entered or not
    # in order to handle an IndexOutOfBounds error for the sys.argv array
    if (len(sys.argv) < 2):
        print("Please enter a filename as an argument")
        pass
    else:

        # Here the weighted_graph is initialized, and num_vertices will be used for
        # error handling later on
        weighted_graph, num_vertices = parse_highway_graph_matrix(sys.argv[1])

        # The D and P matrices are initialized by running Floyd-Warshall's algorithm
        D, P = weighted_graph.floyd_warshall()

        # This run_loop variable will dictate whether the while loop runs or not
        run_loop = True

        # This while loop will prompt the user for the source and destination vertex ID's.
        # Then, it will print out of the vertices in the shortest path, and also the total weight.
        # Lastly, the user is asked if they would like to continue and try new values for the source
        # and destination. If yes, then the loop will continue running. If no, then it will stop.
        while run_loop:
            print("Let's find the shortest path for this graph.")

            print(f"The range of vertex ID's is: 0 to {num_vertices} (exclusive)")

            source = int(input("Enter a vertex ID for the source vertex: "))
            while source < 0 or source >= num_vertices:
                source = int(input("Please enter a source vertex ID that is within bounds: "))

            destination = int(input("Enter a vertex ID for the destination vertex: "))
            while destination < 0 or destination >= num_vertices:
                destination = int(input("Please enter a destination vertex ID that is within bounds: "))

            weight, path = pair_shortest_path(D,P,source,destination)
            print("\n")
            print(f"Shortest Path from {source} to {destination}: ", end="")
            for v in path:
                print(f"{v}", end=", ")
            print(f"\nTotal weight of this path: {weight}")

            print("Would you like to try new values?")
            user_answer = input("Enter \"y\" for Yes, \"n\" for No: ")
            while user_answer.lower() != "y" and user_answer.lower() != "n":
                user_answer = input("Please enter \"y\" for Yes, \"n\" for No: ")

            if user_answer.lower() == "y":
                continue
            elif user_answer.lower() == "n":
                run_loop = False


    pass # here temporarily until you implement this.
    




    
