# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodones = 0
        def dfs(node, localMax):
            if not node:
                return 0
            if node.val >= localMax:
                localMax = node.val
                self.goodones += 1
            if node.left:
                dfs(node.left, localMax)
            if node.right:
                dfs(node.right, localMax)
        return dfs(root, root.val)
      

