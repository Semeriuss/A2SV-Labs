class Solution:
    # O(max(N, M)) time and space
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charMap = {}
        seen = set()
        for a, b in zip(s, t):
            if (a in charMap and charMap[a] != b) or (a not in charMap and b in seen):
                return False
            elif a not in charMap:
                charMap[a] = b
                seen.add(b)
        return True
