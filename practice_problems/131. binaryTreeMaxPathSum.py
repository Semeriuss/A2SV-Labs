# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float("-inf")

        def maxPathDFS(node: TreeNode) -> int:
            if not node: return 0
            leftMax = max(0, node.val + maxPathDFS(node.left))
            rightMax = max(0, node.val + maxPathDFS(node.right))
            self.maxsum = max(self.maxsum, leftMax + node.val + rightMax)
            return max(leftMax, rightMax) + node.val 

        maxPathDFS(root)
        return self.maxsum
 
                    
# [1,2,3]
# [-10,9,20,null,null,15,7]
# [-10,9,20,null,null,15,7,-1,-2,-3,-4,10,20,9,19,null,null,31]
# [-9,6,-3,-2,null,-6,2,null,null,2,null,-6,-6,-6,2,2]