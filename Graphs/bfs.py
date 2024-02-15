def dfs(graph, visited, start):
    print(visited)
    """
    Performs Depth First Search traversal on a graph using an Adjacency Matrix.

    Args:
        graph: The adjacency matrix representing the graph.
        visited: A list to keep track of visited nodes.
        start: The starting node for the traversal.
    """
    nme = ['A','B','C','D','E']
    visited[start] = True
    print(nme[start], end=" ")  # Print the current node

    for i in range(len(graph)):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, visited, i)  # Recursively explore unvisited neighbors

# Example usage
        # A  B  C  D  E
graph = [[0, 1, 0, 0, 0], # A  # Adjacency matrix representation of the graph
         [0, 0, 1, 1, 0], # B
         [0, 0, 0, 0, 1], # C
         [1, 0, 0, 0, 0], # D
         [0, 0, 0, 1, 0]] # E

visited = [False] * len(graph)  # Initialize all nodes as unvisited

print("DFS traversal:")
dfs(graph, visited, 0)  # Start DFS from node 0