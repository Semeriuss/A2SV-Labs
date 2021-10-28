class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k % 2 == 0 or k % 5 == 0:
            return -1
       
        def generateOnes(n):
            possibleNums = []
            var = []
            for i in range(n):
                var.append('1')
                possibleNums.append(int("".join(var)))
            return possibleNums
        
        possibles = generateOnes(k)
                
        for possible in possibles:
            if possible % k == 0:
                return len(list(str(possible)))
        return -1