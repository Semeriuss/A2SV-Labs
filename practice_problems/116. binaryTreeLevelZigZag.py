# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root: return result
        self.bfs(root, root.left, root.right, result)
        return result

    def bfs(parent: TreeNode, leftChild: TreeNode, rightChild: TreeNode, result: List[int]):
        result.append([parent.val])

        queue = deque()

        if rightChild:
            queue.append(rightChild)
        if leftChild:
            queue.append(leftChild)

        while queue:
            curr_node = queue.popleft()
            result.append([curr_node.val])
            if queue:
                next_node = queue.popleft()
                if next_node.left:
                    queue.append(next_node.left)
                if next_node.right:
                    queue.append(next_node.right)
                result.append(next_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        
            
            

