#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
from typing import List


class Solution:
    # O(NLogN) time and O(N) space
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_array = []
        letter_array = []
        for log in logs:
            items = log.split()
            if items[-1].isdigit():
                digit_array.append(log)
            else:
                letter_array.append(tuple([items[1:], [items[0]]]))

        letter_array.sort()
        res = []
        for letter in letter_array:
            letter, identifier = letter
            res.append(identifier[0] + " " + " ".join(letter))
        res.extend(digit_array)

        return res

# @lc code=end
