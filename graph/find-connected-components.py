"""

Implement a function that takes an undirected graph and prints all the connected components of a graph.

Input#
An undirected graph

Output#
All connected components in a graph in a list as a list
Time complexitiy O(V+E)
"""
from graph import Graph
import copy
def connected_components(graph):
    visited = []
    result = []
    for i in range(graph.V):
        visited.append(False)
    for v in range(graph.V):
        if not visited[v]:
            result.append(dfs(g, v, visited))
    return result

def dfs(g, source, visited):
    graph = copy.deepcopy(g)
    stack = []
    result = []
    stack.append(source)
    while stack:
        source = stack[-1]
        stack.pop()
        if not visited[source]:
            result.append(source)
            visited[source] = True
        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            graph.graph[source] = graph.graph[source].next
    return result
# Main program to test above function
if __name__ == "__main__":

    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    g.add_edge(5, 6)

    result = connected_components(g)

    print("Following are connected components")
    print(result)
