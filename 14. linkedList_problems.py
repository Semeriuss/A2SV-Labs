class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
	    
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def appendToTail(self, element):
        current = self.head
        self.length += 1
        if current:            
            while current.next:
                current = current.next
            current.next = Node(element)
        else:
            self.head = Node(element)

    def deleteNode(self, value):
        current = self.head
        self.length -= 1
        if current.value == value:
            self.head = current.next
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
            current = current.next

    def deleteMiddleNode(self, node):
        """delete a node in the middle given the node."""
        if node is None or node.next is None:
            return 
        next_node = node.next
        node.value = next_node.value     
        node.next = next_node.next

    def printLinkedList(self):
        current = self.head
        while current is not None:
            print(current.value, end = " ")
            current = current.next
        print()

            
    # O(n^2) double loop method
    def removeDuplicates(self):  
        root = self.head
        while root:
            preshoot = root
            shoot = root.next
            while shoot:
                if root.value == shoot.value:
                    preshoot.next = shoot.next
                    shoot = shoot.next
                    self.length -= 1
                else:
                    preshoot = shoot
                    shoot = shoot.next            
            root = root.next

    # O(n) hash set method
    def removeDuplicates(self):
        """Remove duplicate elements from linked list."""
        rear = self.head
        front = rear.next
        hashset = set()
        hashset.add(rear.value)
        while front:
            if front.value in hashset:
                rear.next = front.next
                self.length -= 1
            else:
                hashset.add(front.value)
                rear = front
            front = front.next

    def subList(self, k):
        """Returns elements from the kth index to last."""
        current = self.head
        index = 0
        while current:
            if index >= k:
                print(current.value, end=" ")
            current = current.next
            index += 1
        print()


    def partition(self, k):
        """Partition linked around value k.
           All nodes less than k come before all nodes
           greater than or equal to k
        """
        current = self.head
        head = current
        tail = current
        while current:
            nextNode = current.next
            if current.value < k:
                current.next = head
                head = current
            else:
                tail.next = current
                tail = current
            current = nextNode
        tail.next = None
        self.head = head
                
                


    def indexFromLast(self, k):
        """Return kth element starting from last.

           assuming 0-based index
        """
        index = self.length - k - 1
        current = self.head
        counter = 0
        while counter < index:
            current = current.next
            counter += 1

        return current.value
        
        
            
        




ll = LinkedList()
ll.appendToTail(1)
ll.appendToTail(4)
ll.appendToTail(1)
ll.appendToTail(3)
ll.deleteNode(4)
ll.appendToTail(1)
ll.appendToTail(7)
ll.appendToTail(8)
ll.appendToTail(9)
ll.appendToTail(1)
ll.appendToTail(3)
ll.appendToTail(4)
ll.appendToTail(7)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(7)
ll.appendToTail(7)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(7)
ll.appendToTail(7)
ll.appendToTail(3)
ll.appendToTail(7)
ll.appendToTail(7)
ll.appendToTail(7)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.appendToTail(3)
ll.printLinkedList()
##ll.removeDuplicates()
##ll.printLinkedList()
##ll.subList(2)
##print(ll.indexFromLast(4))
ll.partition(4)
ll.printLinkedList()
