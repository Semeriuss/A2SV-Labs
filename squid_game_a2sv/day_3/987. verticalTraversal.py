class Solution:
    # O(nlogn) time | O(n) space
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapper = defaultdict(list)
        def dfs(node, x, y):
            if not node:
                return
            mapper[x].append((y, node.val))
            dfs(node.left, x-1, y+1)
            dfs(node.right, x+1, y+1)
        
        dfs(root, 0, 0)
        res = []
        for x in sorted(mapper):
            res.append([val for _, val in sorted(mapper[x])])
        return res