# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        que = deque([(root, root.val)])
        goodNodes = 0
        while que:
            currNode, localMax = que.popleft()
            if currNode.val >= localMax:
                goodNodes += 1
                localMax = currNode.val
            if currNode.left:
                que.append((currNode.left, localMax))
            if currNode.right:
                que.append((currNode.right, localMax))
        return goodNodes

