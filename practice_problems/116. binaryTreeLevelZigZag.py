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

    def bfs(self, parent: TreeNode, leftChild: TreeNode, rightChild: TreeNode, result: List[int]):
        result.append([parent.val])
        result.append([])

        queue = deque()
        
        if rightChild:
            queue.append(rightChild)
            result[-1].append(rightChild.val)

        if leftChild:
            queue.append(leftChild)
            result[-1].append(leftChild.val)

        turn = False
        if result[-1]:
            result.append([])

        while queue:
            curr_node = queue.popleft()
            result[-1].append(curr_node.val)
            innerQueue = queue.copy()
            queue.clear()

            if curr_node.left:
                queue.appendleft(curr_node.left)
            if curr_node.right:
                queue.appendleft(curr_node.right)
            
            while innerQueue:
                next_node = innerQueue.pop()
                result[-1].append(next_node.val)
                if next_node.right:
                    queue.appendleft(next_node.right)
                if next_node.left:
                    queue.appendleft(next_node.left) 
    
            result.append([])
        result.pop()
            

