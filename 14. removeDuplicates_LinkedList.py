class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
	    
class LinkedList:
    def __init__(self):
        self.head = None

    def appendToTail(self, element):
        current = self.head
        if current:            
            while current.next:
                current = current.next
            current.next = Node(element)
        else:
            self.head = Node(element)

    def deleteNode(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
            current = current.next            

    def printLinkedList(self):
        current = self.head
        while current is not None:
            print(current.value, end = " ")
            current = current.next
        print()

    def removeDuplicates(self):
        root = self.head
        while root:
            shoot = root.next
            while shoot and shoot.next:
                if root.value == shoot.value:
                    shoot.next = shoot.next.next
                else:
                    shoot = shoot.next
            if shoot and root.value == shoot.value:
                shoot = shoot.next                
            root = root.next
            

    def removeDuplicates(self):
        root = self.head
        while root:
            preshoot = root
            shoot = root.next
            while shoot:
                if root.value == shoot.value:
                    preshoot.next = shoot.next
                    shoot = shoot.next
                else:
                    preshoot = shoot
                    shoot = shoot.next            
            root = root.next            
        




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
ll.removeDuplicates()
ll.printLinkedList()

