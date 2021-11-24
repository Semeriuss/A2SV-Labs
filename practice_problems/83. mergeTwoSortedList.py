from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        head = mergedList
        while list1 and list2:
            if list1.val >= list2.val:
                mergedList.next = ListNode(list2.val)
                list2 = list2.next
                mergedList = mergedList.next
            
            elif list1.val < list2.val:
                mergedList.next = ListNode(list1.val)
                list1 = list1.next
                mergedList = mergedList.next
            
        while list1:
            mergedList.next = ListNode(list1.val)
            list1 = list1.next
            mergedList = mergedList.next

        while list2:
            mergedList.next = ListNode(list2.val)
            list2 = list2.next
            mergedList = mergedList.next
        
        head = head.next
        return head
    
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# list1 = ListNode()
# list2 = ListNode()
ans = Solution().mergeTwoLists(list1, list2)


while ans:
    print(ans.val, end=" - ")
    ans = ans.next