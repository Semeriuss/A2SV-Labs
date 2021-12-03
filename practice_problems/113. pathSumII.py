# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if not root: return result
        self.dfs(root, targetSum, root.val, [root.val], result)
        return result
    
    def dfs(self, node: TreeNode, targetSum: int, runningSum: int, path: List[int], result: List[int]):
        if not node.left and not node.right and runningSum == targetSum:
            result.append(path[:])
        
        if node.left:
            path.append(node.left.val)
            self.dfs(node.left, targetSum, runningSum + node.left.val, path, result)
            # remove from path when returning from the recursive call
            path.pop()
        
        if node.right:
            path.append(node.right.val)
            self.dfs(node.right, targetSum , runningSum + node.right.val, path, result)
            path.pop()
