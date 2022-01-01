# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        count = 0
        def dfs(root):
            if not root:
                return 0
            if None in [root.left, root.right]:
                return max(dfs(root.left), dfs(root.right)) + 1
            else:
                return min(dfs(root.left), dfs(root.right)) + 1
        dfs_count = dfs(root)            
            

        def bfs(root):
            if not root:
                return 0
            
            queue = deque([root])
            count = 0
            while queue:
                current = queue.popleft()
                if current.left is None and current.right is None:
                    return count + 1
                else:
                    count += 1
                    if current.left: queue.append(current.left)
                    if current.right: queue.append(current.right)
            return count

        bfs_count = bfs(root)
        return bfs_count
        


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(17)))
root = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
print(Solution().minDepth(root))
        