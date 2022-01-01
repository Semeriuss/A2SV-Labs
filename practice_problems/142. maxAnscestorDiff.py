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
        def dfs(node, minsofar, maxsofar):
            if not node: return
            self.res = max(self.res, abs(node.val - minsofar), abs(node.val - maxsofar))
            minsofar, maxsofar = min(minsofar, node.val), max(maxsofar, node.val)
            dfs(node.left, minsofar, maxsofar)
            dfs(node.right, minsofar, maxsofar)
        dfs(root, root.val, root.val)
        return self.res