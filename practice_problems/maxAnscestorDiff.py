# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.min, self.max = float('inf'), float('-inf')
        def dfs(node, minsofar, maxsofar):
            if not node.left and not node.right: return node.val
            if node.left:
                minsofar = min(minsofar, node.left.val)
                maxsofar = max(maxsofar, node.left.val)
                self.res = max(self.res, dfs(node.left, minsofar, maxsofar))
            if node.right:
                minsofar = min(minsofar, node.right.val)
                maxsofar = max(maxsofar, node.right.val)
                self.res = max(self.res, dfs(node.right, minsofar, maxsofar))
            return max(abs(node.val - minsofar), abs(node.val - maxsofar))
        dfs(root, float("inf"), float("-inf"))
        return self.res