def hasPath(graph, src, dst):

    visited = set()
    def dfs(graph, source, target):
        visited.add(source)
        if source == target:
            return True
        
        canReach = False
        for neighbor in graph[source]:
            if neighbor not in visited:
                canReach = canReach or dfs(graph, neighbor, target)
        return canReach
    
    return dfs(graph, src, dst)

graph = {
        'f' : ['g', 'i'],
        'g' : ['h'],
        'h' : [],
        'i' : ['g', 'k'],
        'j' : ['i'],
        'k' : []
        }

print(hasPath(graph, 'f', 'k'))