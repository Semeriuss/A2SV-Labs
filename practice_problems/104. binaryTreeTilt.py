# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def valueSum(node):
            if not node: return (0, 0)
            left = valueSum(node.left)
            right = valueSum(node.right)
            return (left[0] + right[0] + node.val, abs(left[0] - right[0]) + left[1] + right[1])
        return valueSum(root)[1]

root = TreeNode(1, TreeNode(2), TreeNode(3))
root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))
print(Solution().findTilt(root))

        