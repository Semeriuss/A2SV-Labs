
from collections import defaultdict
import collections


def topologicalsort(graph):
    NUMBER_OF_NODES = len(graph.keys())
    
    incoming = defaultdict(int)
    for node in graph.keys():
        incoming[node]
        for ins in graph[node]:
            incoming[ins] += 1

    topsort = []
    def dfs(node):
        nonlocal graph, incoming, topsort

        if incoming[node] != 0:
            return 
        
        topsort.append(node)
        for neighbor in graph[node]:
            incoming[neighbor] -= 1
            dfs(neighbor)
        return 
    
    independentNodes = [node for node in incoming.keys() if incoming[node] == 0]
    for node in independentNodes:
        dfs( node)
    
    if NUMBER_OF_NODES != len(topsort):
            return "Impossible to sort topologically"
        
    # return " ".join(topsort)  # dfs implementation
    


    
    def bfs():
        nonlocal incoming, graph

        queue = collections.deque()
        topsort = []
        for node in incoming:
            if incoming[node] == 0:
                queue.append(node)

        while queue:
            current = queue.popleft()
            topsort.append(current)
            for neighbor in graph[current]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)

        if NUMBER_OF_NODES != len(topsort):
            return "Impossible to sort topologically"
        
        return " ".join(topsort)

    # return bfs() # bfs implementation




graph = {
        'f' : ['g', 'i'],
        'g' : ['h'],
        'h' : [],
        'i' : ['k'],
        'j' : ['i', 'h'],
        'k' : ['h']
        }

graph2 = {
        'f' : ['g', 'i'],
        'g' : ['h'],
        'h' : ['i'],
        'i' : ['k'],
        'j' : ['i', 'h'],
        'k' : ['h']
        }

print(topologicalsort(graph))