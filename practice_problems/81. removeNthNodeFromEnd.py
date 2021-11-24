# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def remove(head, n):
            if not head: return head, 0
            node, count = remove(head.next, n)
            head.next = node
            count += 1
            if count == n: head = head.next

            return head, count
        print()
        return remove(head, n)[0]

    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))
n = 3

# head = ListNode(1)
# n = 1

# head = ListNode(1, ListNode(2))
# n = 1

# print(Solution().removeNthFromEnd(head, n))
        
ans = Solution().removeNthFromEnd(head, n)
while ans:
    print(ans.val, end = " ")
    ans = ans.next
