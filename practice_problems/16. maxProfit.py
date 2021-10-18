def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy = 0
    sell = 0
    profits = []
    for i in range(len(prices)-1):
        buy = prices[i]
        for j in range(i+1, len(prices)):
            if prices[j] > prices[i]:
                sell = prices[j]

            if sell > 0:
                profits.append(sell - buy)

    return max(profits) if profits else 0

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy = 0
    sell = 0
    profit = 0
    for i in range(len(prices)):
        buy = prices[i]
        if len(prices[i+1:])>0 and max(prices[i+1:]) > buy:
               sell = max(prices[i+1:])
               if sell - buy > profit:
                   profit = sell - buy

    return profit

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    minPrice = prices[0]
    maxProfit = 0
    for price in prices:
        if price <= minPrice:
            minPrice = price
        else:
            difference = price - minPrice
            maxProfit = max(difference, maxProfit)

    return maxProfit
    
tests = [[7,1,5,3,6,4], [7,6,4,3,1]]
for test in tests:
    print(maxProfit(test))

            
            
