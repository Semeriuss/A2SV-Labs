class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        
class BST:

    def __init__(self, root: Node = None):
        self.root = root
        
    def put(self, key: int, val: int) -> None:
        self.root = self._put(self.root, key, val)
        
    def _put(self, node: Node, key: int, val: int) -> Node:
        if not node:
            node = Node(key, val)
            return node
        
        if node.key > key:
            node.left = self._put(node.left, key, val)
        elif node.key < key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        return node

    def get(self, key: int) -> int:
        node = self._get(self.root, key)
        return node.val if node is not None else -1
        
    def _get(self, node: Node, key: int) -> Node:
        if node is None or node.key == key:
            return node
        return self._get(node.right, key) if node.key<key else self._get(node.left, key)        
    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)
    
    def _remove(self, node: Node, key: int) ->Node:
        if not node:
            return node
        
        if node.key < key:
            node.right = self._remove(node.right, key)
        elif node.key > key:
            node.left = self._remove(node.left, key)
        else:
            if not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                node.key, node.val = self.findMinKey(node.right)
                node.right = self._remove(node.right, node.key)
        return node
    
    def findMinKey(self, node: Node) -> int:
        return (node.key, node.val) if not node.left else self.findMinKey(node.left)
        

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val, end="=>")
        printInorder(root.right)

bst = BST()

bst.put(22,83)
bst.put(39,4)
bst.put(34,88)
bst.put(72,99)
bst.remove(33)
bst.put(58,77)
bst.put(23,61)
bst.remove(34)
bst.remove(66)
bst.remove(90)
bst.put(72, 83)
bst.put(50, 98)
bst.put(93, 97)
bst.put(74, 95)
bst.remove(81)
bst.put(56, 1)
bst.put(86, 80)
bst.put(93, 91)
bst.put(13, 1)
bst.remove(93)
bst.put(63, 11)
bst.put(62, 63)
print(bst.get(63))
bst.put(71, 98)
bst.put(97, 96)
bst.put(65, 47)
bst.remove(93)
bst.put(30, 78)
bst.put(31, 40)
bst.put(67, 86)
bst.put(84, 11)
bst.put(3, 19)
bst.put(30, 97)
bst.put(3, 36)
print(bst.get(63))
bst.put(71, 96)
bst.put(97, 96)
bst.put(65, 47)
bst.remove(93)
bst.put(30, 78)
bst.put(31, 40)
bst.put(67, 86)
bst.put(84, 11)
bst.put(3, 36)
print(bst.get(63))
bst.put(92, 43)
bst.remove(71)
printInorder(bst.root)
bst.remove(86)
print()
printInorder(bst.root)
bst.put(77, 91)
bst.put(18, 29)
bst.put(75, 44)
print(bst.get(59))
bst.put(35, 81)
bst.remove(58)
bst.put(12, 69)
bst.remove(58)
print(bst.get(86))

printInorder(bst.root)

["MyHashMap","put",  "put",  "put", "put",  "remove","put", "put",   "remove", "remove","remove", "put",   "put",  "put",  "put",   "remove","put", "put",  "put",  "put", "remove","put",  "put",  "get","put",  "put",  "put",  "remove","put",   "put",  "put",  "put",  "put", "put",  "put", "get","put",  "remove","remove","put",   "put",  "put",  "get","put",   "remove", "put",  "remove","get", "put", "put",  "remove","get", "put",  "remove","put",   "put",  "put",  "put",  "put",  "put",  "put", "get","remove","put",   "put",  "put", "put", "remove","put",  "put",  "put",   "put",  "put",  "put", "put",   "put", "put",   "put",  "put", "put", "put", "put",  "put",  "put",  "get","put",   "put",  "put",  "put", "put",  "put", "put",   "put",  "remove","get","put",  "remove","put",   "put",  "remove","remove"]
[[],         [22,83],[39,4],[34,88],[72,99],[33],    [58,77],[23,61],[34],     [66],    [90],      [72,83],[50,98],[93,97],[74,95],[81],     [56,1],[86,80],[93,91],[13,1],[93],    [63,11],[62,63],[63], [71,98],[97,96],[65,47],[93],     [30,78],[31,40],[67,86],[84,11],[3,19],[30,97],[3,36],[63], [92,43],[71],     [86],    [77,91],[18,29],[75,44],[59],  [35,81],[58],     [12,69],[58],     [86], [84,9],[83,40],[82],    [82],   [55,0],[65],     [88,83],[61,83],[18,68],[61,19],[92,74],[68,15],[7,99],[97], [92],     [17,96],[73,22],[7,16],[7,16], [3],     [0,16],[22,27],[74,26],[63,28],[84,70],[44,23],[51,38],[65,67],[75,85],[50,57],[75,55],[4,84],[9,16],[69,39],[40,34],[99,55],[74],  [42,53],[17,9],[70,92],[89,11],[15,64],[75,22],[27,59],[14,84], [9],     [40], [59,47],[60],     [33,32],[63,28],[15],      [33]]
[None,       None,    None,   None,   None,  None,    None,   None,   None,     None,    None,      None,   None,   None,   None,   None,      None,  None,   None,   None,  None,   None,   None,   11,   None,   None,   None,   None,     None,   None,    None,  None,    None,  None,  None,  11,   None,   None,     None,    None,    None,   None,  -1,    None,   None,      None,   None,    43,   None,   None,   None,   -1,    None,    None,    None,   None,   None,    None,   None,   None,   None, 96,   None,    None,    None,   None,   None,   None,   None,   None,  None,   None,   None,   None,   None,   None,   None,  None,     None,   None,  None,  None,  None,  None,    26,     None,   None,  None,  None,   None,    None,  None,    None,   None,   34,    None,   None,    None,    None,   None,    None]
[None,       None,    None,   None,   None,  None,    None,   None,   None,     None,    None,      None,   None,   None,   None,   None,      None,  None,   None,   None,  None,   None,   None,   11,   None,   None,   None,   None,     None,   None,    None,  None,    None,  None,  None,  11,   None,   None,     None,    None,    None,   None,  -1,    None,   None,      None,   None,    -1,   None,   None,   None,   -1,    None,    None,    None,   None,   None,    None,   None,   None,   None, 96,   None,    None,    None,   None,   None,   None,   None,   None,  None,   None,   None,   None,   None,   None,   None,  None,     None,   None,  None,  None,  None,  None,    26,     None,   None,  None,  None,   None,    None,  None,    None,   None,   34,    None,   None,    None,    None,   None,    None]
