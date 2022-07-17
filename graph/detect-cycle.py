"""

You have to implement the detect_cycle function which tells you whether or not a graph contains a cycle.

Input#
A graph

Output#
True if a cycle exists and False, if it doesn’t

Time complexity O(V+E)
"""
from graph import Graph
def detect_cycle(graph):
    visited = [False] * graph.V
    my_stack = [False] * graph.V
    for node in range(graph.V):
        if detect_cycle_recursive(graph, node, visited, my_stack):
            return True
    return False

def detect_cycle_recursive(graph, node, visited, my_stack):
    if my_stack[node]:
        return True
    if visited[node]:
        return False
    visited[node] = True
    my_stack[node] = True
    head = graph.graph[node]
    while head is not None:
        adjacent = head.vertex
        if detect_cycle_recursive(graph, adjacent, visited, my_stack):
            return True
        head = head.next
    my_stack[node] = False
    return False

# Main program to test the above code
if __name__ == "__main__":

    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(3, 0)

    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    print(detect_cycle(g1))
    print(detect_cycle(g2))
