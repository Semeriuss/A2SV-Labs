# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.res = 0
        
        def dfs(child: TreeNode, parent: TreeNode) -> None:
            if not child and not parent:
                return 
            
            elif not child:
                return 0
            
            elif not parent:
                if child.left: dfs(child.left, child)
                if child.right: dfs(child.right, child)
            
            else:
                if not parent.val % 2:
                    leftGrandChild = child.left
                    rightGrandChild = child.right
                    if leftGrandChild:
                        self.res += leftGrandChild.val
                        dfs(child.left, child)
                    if rightGrandChild:
                        self.res += rightGrandChild.val
                        dfs(child.right, child)
                else:
                    if child.left: dfs(child.left, child)
                    if child.right: dfs(child.right, child)
        
        dfs(root, None)
        return self.res
                        

root = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
# root = TreeNode(1, TreeNode(5), TreeNode(6, TreeNode(3, TreeNode(2), TreeNode(2))))
print(Solution().sumEvenGrandparent(root))