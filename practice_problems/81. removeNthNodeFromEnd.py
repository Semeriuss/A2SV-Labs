# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None

        slow = fast = head
        
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next

        while head:
            print(head.val, end = " ")
            head = head.next

    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))
n = 3

# head = ListNode(1)
# n = 1

# head = ListNode(1, ListNode(2))
# n = 1

print(Solution().removeNthFromEnd(head, n))
        
        