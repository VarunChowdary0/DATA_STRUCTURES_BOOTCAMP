def toGraph(edges,n):
    graph = [[] for i in range(n)]
    
    for edge in edges:
        src = edge[0]
        dst = edge[1]
        wt = edge[2]
        graph[src-1].append([src,dst,wt])
        graph[dst-1].append([dst,src,wt])

    return graph

def hasPath(graph,src,dest,visited):
    pass

edges = [
    [1,2,90],
    [1,3,73],
    [2,4,902],
    [3,4,223],
    [4,5,900],
    [5,8,76],
    [5,7,61],
    [5,6,221],
    [7,6,761],
    [8,7,145]
]
n = 8

visited = [ False for u in range(n)]
graph = toGraph(edges,n)

for x in graph:
    print(x)