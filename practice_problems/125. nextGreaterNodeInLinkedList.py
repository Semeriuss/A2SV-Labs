# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        root, nodes = head, []
        while root:
            nodes.append(root.val)
            root = root.next
        
        answer, stack = [0]*len(nodes), [nodes[len(nodes) - 1]]
        for i in range(len(nodes) - 1, - 1, -1):
            while stack and nodes[i] >= stack[-1]:
                stack.pop()
            if stack: answer[i] = stack[-1]
            stack.append(nodes[i])
        return answer