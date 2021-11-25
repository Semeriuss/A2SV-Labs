from typing import List, Optional
import  heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        current = head = ListNode()
        queue = []
        count = 0
        for ptr in lists:
            heapq.heappush(queue, (ptr.val, count, ptr))
            count += 1
        while queue:
            _, _, curr = heapq.heappop(queue)
            current.next = curr
            current = current.next
            curr = curr.next
            count += 1
            if curr:
                heapq.heappush(queue, (curr.val, count, curr))
        
        return head.next


