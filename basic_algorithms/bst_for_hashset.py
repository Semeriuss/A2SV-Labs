class TreeNode:
    
    def __init__(self, val : int = -1, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class BST:
    
    def __init__(self, root = None):
        self.root = root
    
    def add(self, value : int) -> None:
        self.root = self._add(self.root, value)
        
    def _add(self, current: TreeNode, value: int) -> TreeNode:
        if current is None:
            current = TreeNode(value)
            return current
        elif value > current.val:
            current.right = self._add(current.right, value)
        elif value < current.val: 
            current.left = self._add(current.left, value)
        return current
        
    def search(self, value: int) -> bool:
        return self._search(self.root, value)
    
    def _search(self, current: TreeNode, value: int) -> bool:
        if current is None:
            return False
        elif current.val < value:
            return self._search(current.right, value)
        elif current.val > value:
            return self._search(current.left, value)
        return True
    
    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    
    def remove(self, value : int) -> None:
        self.root = self._remove(self.root, value)
        
    def _remove(self, current: TreeNode, value: int) -> TreeNode:
        if current is None:
            return current
        if current.val < value:
            current.right = self._remove(current.right, value)
        elif current.val > value:
            current.left = self._remove(current.left, value)
        else:
            if current.right == None:
                current = current.left
                return current
            elif current.left == None:
                current = current.right
                return current
            else:
                temp = self.minValueNode(current.right)
                current.val = temp.val
                current.right = self._remove(current.right, current.val)
        return current


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val, end="=>")
        printInorder(root.right)

root = bst = BST()

bst.add(1)
bst.add(2)
bst.add(2)
bst.add(4)
bst.add(9)
bst.add(6)
bst.add(8)
bst.add(0)
bst.add(199)
bst.add(234)
bst.add(4567)
bst.add(87)


printInorder(bst.root)
bst.remove(1)
print(bst.search(0))
printInorder(bst.root)
