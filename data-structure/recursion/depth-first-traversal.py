import graph as g
def helperFunction(myGraph, current, visited):
    if visited[current] == False:
        visited[current] = True
        print(current)
    for i in myGraph.graph[current]:
        if visited[i] == False:
            helperFunction(myGraph, i, visited)

def DFS(myGraph):
    visited = [False]*(myGraph.vertices)
    helperFunction(myGraph, 0, visited)


# Driver code

# Create a graph given in the above diagram
myGraph = g.Graph(6)
myGraph.addEdge(0, 1)
myGraph.addEdge(1, 2)
myGraph.addEdge(1, 3)
myGraph.addEdge(2, 4)
myGraph.addEdge(3, 4)
myGraph.addEdge(3, 5)

print("DFS Graph Traversal")
DFS(myGraph)
