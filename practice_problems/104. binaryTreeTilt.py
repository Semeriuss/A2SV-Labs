# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        def valueSum(node):
            nonlocal res
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            
            left = valueSum(node.left)
            right = valueSum(node.right)
            res += abs(left - right)
            return left + right 
        return valueSum(root)

root = TreeNode(1, TreeNode(2), TreeNode(3))
root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))
print(Solution().findTilt(root))

        