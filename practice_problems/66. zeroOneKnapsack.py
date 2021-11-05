
def zeroOneKnapsack(weights, profits, capacity, processing):
    if processing == 0 or capacity == 0:
        result = 0

    elif weights[processing] > capacity:
        result = zeroOneKnapsack(weights, profits, capacity, processing - 1)
    
    else:
        path1 = profits[processing] + zeroOneKnapsack(weights, profits, capacity - weights[processing], processing - 1)
        path2 = zeroOneKnapsack(weights, profits, capacity, processing - 1)
        result = max(path1, path2)

    return result



weights = [1,2,3,5]
profits = [1,6,10,16]
capacity = 7
print(zeroOneKnapsack(weights, profits, capacity, len(weights) - 1))

        