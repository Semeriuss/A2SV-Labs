# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode, tail: TreeNode = None) -> TreeNode:              
            if not root: return tail
            finalRoot = self.increasingBST(root.left, root)
            root.left = None
            root.right = self.increasingBST(root.right, finalRoot)
            return finalRoot


root = TreeNode(5, TreeNode(1), TreeNode(2))
print(Solution().increasingBST(root))