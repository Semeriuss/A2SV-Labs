
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # O(N) time and space
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        hashmap = {head: Node(head.val)}
        root = head
        while root:
            nex, random = root.next, root.random
            if nex and nex not in hashmap:
                hashmap[nex] = Node(nex.val)
            if random and random not in hashmap:
                hashmap[random] = Node(random.val)
            hashmap[root].next = hashmap[nex] if nex else None
            hashmap[root].random = hashmap[random] if random else None
            root = root.next
        return hashmap[head]
