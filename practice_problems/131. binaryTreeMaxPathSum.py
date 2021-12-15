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

        que = deque([root])
        maxsum = root.val
        dp = {}
        
        while que:
            curr = que.popleft()
            currMax = curr.val
            leftMax = 0
            rightMax = 0
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)

            leftMax = max(0, self.maxPathDFS(curr.left, dp, leftMax))
            rightMax = max(0, self.maxPathDFS(curr.right, dp, rightMax))
            currMax += leftMax + rightMax
            maxsum = max(maxsum, currMax)
        return maxsum
    
    def maxPathDFS(self, node: TreeNode, dp: dict, currMax: int = 0) -> int:
        if node in dp: return dp[node]
        if not node: return 0
        if not node.left and not node.right: 
            dp[node] = max(currMax, currMax + node.val)
            return dp[node]
        dp[node] = currMax =  max(currMax, currMax + max(node.val + self.maxPathDFS(node.left, dp, currMax), node.val + self.maxPathDFS(node.right, dp, currMax)))
        return currMax


                
                    
# [1,2,3]
# [-10,9,20,null,null,15,7]
# [-10,9,20,null,null,15,7,-1,-2,-3,-4,10,20,9,19,null,null,31]
# [-9,6,-3,-2,null,-6,2,null,null,2,null,-6,-6,-6,2,2]