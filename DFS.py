graph = {
    '4' : ['3'],
    '3' : ['10','9','2'],
    '10': [],
    '9' : [],
    '2' : ['1','8'],
    '1' : [],
    '8' : ['7'],
    '7' : ['5'],
    '5' : ['6'],
    '6' : []
}

visited = set() 

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
dfs(visited, graph, '4')