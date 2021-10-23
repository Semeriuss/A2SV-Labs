
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        count = 0
        def dfs(node: 'Node', count):
            if node:
                count += 1
                current_count = count
                if node.children:
                    for child in node.children:
                        count = max(dfs(child, current_count), count)
            return count
        return dfs(root, 0)        
        
graph = Node(val = 1, children=[Node(val = 3, children= [Node(val = 5), Node(val = 6)]), Node(val = 2), Node(val = 4)])
print(Solution().maxDepth(graph))

                
            
