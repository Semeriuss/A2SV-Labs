class Solution:
    # O(N) time | O(N) space
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        zeroToNineteen = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                          11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

        tens = {1: 'Ten', 2: 'Twenty', 3: 'Thirty', 4: 'Forty',
                5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}

        def dfs(num):
            if num == 0:
                return ""
            elif num < 20:
                return zeroToNineteen[num]
            elif num < 100:
                return (tens[num//10] + ' ' + dfs(num % 10)).rstrip()
            elif num < 1000:
                return (dfs(num//100) + ' Hundred ' + dfs(num % 100)).rstrip()
            elif num < 1000000:
                return (dfs(num//1000) + ' Thousand ' + dfs(num % 1000)).rstrip()
            elif num < 1000000000:
                return (dfs(num//1000000) + ' Million ' + dfs(num % 1000000)).rstrip()
            else:
                return (dfs(num // 1000000000) + ' Billion ' + dfs(num % 1000000000)).rstrip()

        return dfs(num)
