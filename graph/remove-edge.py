"""

You must implement the remove_edge function which takes a source and a destination as arguments. If an edge exists between the two, it should be deleted. Print the breadth-first traversal on the resultant graph.

Input#
A graph, a source (integer), and a destination (integer)

Output#
A BFS traversal of the graph with the edge between the source and the destination removed

The time complexity is O(E)
 where E
 is the number of edges at the source vertex.

"""
from graph import Graph
def remove_edge(graph, source, destination):
    if graph.V == 0:
        return graph
    if source >= graph.V or source < 0:
        return graph
    if destination >= graph.V or destination < 0:
        return graph
    temp = graph.graph[source]
    # If head node itself holds the key to be deleted
    if temp is not None:
        if temp.vertex == destination:
            graph.graph[source] = temp.next
            temp = None
            return
    while temp is not None:
        if destination == temp.vertex:
            break
        prev = temp
        temp = temp.next
    if temp is None:
        return
    # Set the new link
    # from removed node's previous node to next node
    prev.next = temp.next
    temp = None

# Main program to test above function
if __name__ == "__main__":

    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)

    print("Before: ")
    g.print_graph()

    remove_edge(g, 1, 3)

    print("After: ")
    g.print_graph()
