
from collections import defaultdict
import collections


def topologicalsort(graph):
    incoming = defaultdict(int)
    for node in graph.keys():
        incoming[node]
        for ins in graph[node]:
            incoming[ins] += 1
    
    def bfs():
        nonlocal incoming, graph

        numberOfNodes = len(graph.keys())

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

        if numberOfNodes != len(topsort):
            return "Impossible to sort topologically"
        
        return " ".join(topsort)

    return bfs()




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

print(topologicalsort(graph2))