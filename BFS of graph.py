#BFS of graph
graph = {
  '0' : ['1','2','3'],
  '1' : [],
  '2' : ['4'],
  '3' : [],
  '4' : []
}
visited = [] 
queue = [] 

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)
  while queue:         
    m = queue.pop(0) 
    print (m, end = " ") 
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited, graph, '0')    
