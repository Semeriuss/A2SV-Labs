# iterative method
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

    first = 1
    second = 2
    

    for i in range(1, n):
        first, second = second, first + second

    return first
        
#Dynamic Programming + recursive method
def climbStairsHelper(memo, n):
    if memo[n]:
        return memo[n]
    if n < 3:
        return n

    memo[n] = climbStairsHelper(memo, n-1) + climbStairsHelper(memo, n-2)
    return memo[n]

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

    memo = [0 for i in range(n+1)]
    return climbStairsHelper(memo, n)


tests = [1,2,3,4,5,6]
for test in tests:
    print(climbStairs(test))


