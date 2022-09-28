#DFS of Graph
graph = {
  '0' : ['2','3','1'],
  '1' : ['0'],
  '2' : ['0','4'],
  '3' : ['0'],
  '4' : ['2']
}
visited = set() 
def dfs(visited, graph, node):   
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
dfs(visited, graph, '0')
