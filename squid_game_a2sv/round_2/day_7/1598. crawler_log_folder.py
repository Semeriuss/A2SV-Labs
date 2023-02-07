from typing import List


class Solution:
    # O(N) time and O(1) space
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for log in logs:
            if log.startswith('../'):
                if level == 0:
                    continue
                level -= 1
            elif log.startswith('./'):
                continue
            else:
                level += 1
        return level
