from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(rootP, rootQ):
            if (not rootP and not rootQ):
                return
            if (rootP and not rootQ) or (not rootP and rootQ) or (rootP.val != rootQ.val):
                return False
            else:
                dfs(rootP.left, rootQ.left) 
                dfs(rootQ.right, rootQ.right)
        
            
            return True
        
        return dfs(p, q)

graphP = TreeNode(1, TreeNode(2), TreeNode(3))
graphQ = TreeNode(1, TreeNode(2), TreeNode(3))

graphR = TreeNode(1, TreeNode(2))
graphS = TreeNode(1, None, TreeNode(2))

graphT = TreeNode(1, TreeNode(2), TreeNode(1))
graphU = TreeNode(1, TreeNode(1), TreeNode(2))

graphV = TreeNode(10, TreeNode(5), TreeNode(15))
graphW = TreeNode(10, TreeNode(5, None, TreeNode(15)))
print(Solution().isSameTree(graphV, graphW))
    
            
            