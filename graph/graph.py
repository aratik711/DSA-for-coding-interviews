class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
    def add_edge(self, source, destination):
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print("-> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

def find_all_paths_recursive(graph, source, destination, visited, path, paths):
    """
    Finds all paths between source and destination in given graph
    :param graph: A directed graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    :param visited: A list to mark visited vertices
    :param path: List to store one path to source from destination
    :param paths: 2D list to store all paths
    """

    # Mark the current node as visited and store in path
    visited[source] = True
    path.append(source)

    # If current vertex is same as destination, then print
    # stores the current path in 2D list (Deep copy)
    if source == destination:
        paths.append(copy.deepcopy(path))
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        while graph.graph[source] is not None:
            i = graph.graph[source].vertex

            if not visited[i]:
                find_all_paths_recursive(graph, i, destination, visited, path, paths)

            graph.graph[source] = graph.graph[source].next

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[source] = False
