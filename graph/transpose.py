"""

You have to implement a function which will take a graph as input and print its transpose.

Input#
A graph

Output#
Return a transpose of the given graph
Time complexitiy O(V+E)

"""
from graph import *
def transpose(my_graph):
    new_graph = Graph(my_graph.V)
    for source in range(my_graph.V):
        while my_graph.graph[source] is not None:
            destination = my_graph.graph[source].vertex
            new_graph.add_edge(destination, source)
            my_graph.graph[source] = my_graph.graph[source].next
    return new_graph


# Main program to test the above function
#if __name__ == "__main__":

#    V = 5
#    g = Graph(V)
#    g.add_edge(0, 1)
#    g.add_edge(0, 2)
#    g.add_edge(1, 3)
#    g.add_edge(1, 4)

#    new_g = transpose(g)
#    new_g.print_graph()
