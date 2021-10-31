import collections


def depthFirstPrintR(graph, node):
    
    print(node, end=" ")
    for node in graph[node]:
        depthFirstPrintR(graph, node)

def depthFirstPrintI(graph, node):
    stack = collections.deque()
    
    stack.append(node)
    while stack:
        currentNode = stack.pop()
        print(currentNode, end=" ")
        for child in graph[currentNode]:
            stack.append(child)
                

graph = {
        'a' : ['b', 'c'],
        'b' : ['d'],
        'c' : ['e'],
        'd' : ['f'],
        'e' : [],
        'f' : []
        }

depthFirstPrintR(graph, 'a')
