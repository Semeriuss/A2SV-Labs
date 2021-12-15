# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        que = deque([root])
        maxsum = root.val
        while que:
            curr = que.popleft()
            currMax, leftMax, rightMax = curr.val, 0, 0
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)

            leftMax = max(0, self.maxPathDFS(curr.left, leftMax))
            rightMax = max(0, self.maxPathDFS(curr.right, rightMax))
            currMax += leftMax + rightMax
            maxsum = max(maxsum, currMax)
        return maxsum
    
    def maxPathDFS(self, node: TreeNode, currMax: int = 0) -> int:
        if not node: return 0
        if not node.left and not node.right: return max(currMax, currMax + node.val)
        currMax = max(currMax, currMax + max(node.val + self.maxPathDFS(node.left, currMax), node.val + self.maxPathDFS(node.right, currMax)))
        return currMax
                
                    
# [1,2,3]
# [-10,9,20,null,null,15,7]
# [-10,9,20,null,null,15,7,-1,-2,-3,-4,10,20,9,19,null,null,31]