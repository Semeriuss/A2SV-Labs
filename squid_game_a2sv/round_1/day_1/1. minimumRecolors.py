class Solution:
    # O(N) time, O(1) auxiliary space
    def minimumRecolors(self, blocks: str, k: int) -> int:

        n = len(blocks)
        res = n
        black_count = temp_count = 0
        i = j = 0
        while i < n:
            while black_count < k and j < n:
                if blocks[j] == 'W':
                    temp_count += 1
                black_count += 1
                j += 1
                if black_count == k:
                    break

            if black_count == k:
                res = min(res, temp_count)
                temp_count -= int(blocks[i] == 'W')
                black_count -= 1
                i += 1
            else:
                break

        return res
