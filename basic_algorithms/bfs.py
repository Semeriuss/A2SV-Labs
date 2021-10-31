from collections import deque
import collections

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def bfs(self, root: 'Node') -> None:

        queue = deque()
        visited = set()

        queue.append(root)
        visited.add(root)
        while queue:
            current = queue.popleft()
            print(current.val, end = " -> ")
            if current.children is not None:
                for neighbor in current.children:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            

def breadthFirstPrintI(graph, root):
    queue = collections.deque()
    
    queue.append(root)
    while queue:
        current = queue.popleft()
        print(current, end=" ")
        for neighbor in graph[current]:
            queue.append(neighbor)

               
        
graph = Node(val = 1, 
        children=[Node(val = 3, 
                    children= [Node(val = 5), Node(val = 6)]), 
                Node(val = 2), 
                Node(val = 4)])
# print(Solution().bfs(graph))

graph = {
        'a' : ['b', 'c'],
        'b' : ['d'],
        'c' : ['e'],
        'd' : ['f'],
        'e' : [],
        'f' : []
        }

breadthFirstPrintI(graph, 'a')


