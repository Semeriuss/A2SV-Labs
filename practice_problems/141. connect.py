# Definition for a Node.
from typing import Optional
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return 
        que = deque([root])
        
        while que:
            temp = que[:]

            for i in range(len(temp) - 1):
                temp[i].next = temp[i + 1]
            
            que.clear()
            while temp:
                curr = temp.pop()
        
                if curr.left:
                    que.append(curr.left)
                
                if curr.right:
                    que.append(curr.right)
            
        
        return root
            
                