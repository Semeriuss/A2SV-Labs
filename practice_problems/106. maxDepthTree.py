# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if not root.children: return 1
        depth = 0
        for node in root.children:
            depth = max(depth, 1 + self.maxDepth(node))
        return depth
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(Solution().maxDepth(root))