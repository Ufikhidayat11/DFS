graph = {
    '4' : ['3','1'],
    '3' : ['4', '10', '9'],
    '1' : ['4', '2'],
    '10' : ['3'],
    '9' : ['3'],
    '2' : ['1', '5', '7', '8'],
    '5' : ['2', '6'],
    '7' : ['2'],
    '8' : ['2'],
    '6' : ['5']
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, '4')