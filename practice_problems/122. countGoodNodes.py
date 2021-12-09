# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode, localMax: int) -> int:
        return self.goodNodes(root.left, max(localMax, root.left.val)) + self.goodNodes(root.right, max(localMax, root.right.val)) + self.goodNodes(root.val, max(localMax, root.val)) if root else 0
        
      

