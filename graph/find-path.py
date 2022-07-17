"""

Implement a function that prints all paths that exist between two nodes (source to destination).

Input#
A graph, a source value, and a destination value

Output#
A 2D list having all paths

Time complexitiy O(V+E)
"""
import copy
from graph import Graph

def find_all_paths_recursive(graph, source, destination, visited, path, paths):
    visited[source] = True
    path.append(source)
    if source == destination:
        paths.append(copy.deepcopy(path))
    else:
        while graph.graph[source] is not None:
            i = graph.graph[source].vertex
            if not visited[i]:
                find_all_paths_recursive(graph, i, destination, visited, path, paths)
            graph.graph[source] = graph.graph[source].next
    path.pop()
    visited[source] = False

def find_all_paths(graph, source, destination):
    visited = [False] * graph.V
    path, paths = [], []
    find_all_paths_recursive(graph, source, destination, visited, path, paths)
    return paths

# Main program to test above function
if __name__ == "__main__":

    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(2, 5)

    source = 0
    destination = 5

    paths = find_all_paths(g, source, destination)
    print(paths)
