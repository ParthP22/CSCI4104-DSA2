from graphfileparser import parse_highway_graph_file
import sys
from graphshw import WeightedGraph

# Name: Parth Patel

if __name__ == "__main__" :

    # This if-statement is being used to make sure that an argument was
    # passed through the command
    if (len(sys.argv) < 2):

        print("Please enter a filename as an argument")
        pass

    else:

        # Here I use a command line argument for a file to create weighted_graph
        # by using the parse_highway_graph_file method
        weighted_graph = parse_highway_graph_file(sys.argv[1])

        # I acquire the completed set of vertices in weighted_graph from dijkstra's algorithm
        completed_vertices = weighted_graph.dijkstra_binheap(0)

        # Finally, I print out all the completed set of 3-tuples, which goes in the
        # following order: vertex-ID, d-value, pi-value
        print("These are the vertex-ID's, d-values, and pi-values of Dijkstra's algorithm performed")
        print("on the graph given by the text file that was passed into command prompt.")
        print(f"Dijkstra's algorithm (Binary Min Heap version) on {sys.argv[1]}")
        print("Format:")
        print("ID, d, pi")
        for i in completed_vertices:
            print(i)
        pass
    pass