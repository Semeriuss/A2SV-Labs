class Solution:
    # O(N) time and space
    def simplifyPath(self, path: str) -> str:
        path = [p for p in path.split('/') if p != '.' and p != '']
        stack = []
        for p in path:
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        
        return '/' + '/'.join(stack)