def find_grants_cap(grantsArray, newBudget):
    # Adding a min cap in case the min cap of
    # grantsArray still overflows from the budget
    grantsArray.append(0)
    
    # Sort the array in descending order 
    # to check the cap sequentially from the top
    grantsArray.sort(reverse=True)

    N = len(grantsArray)
    
    # calculate the budget overflow above the new 
    # budget to decrease it accordingly
    surplus = sum(grantsArray) - newBudget

    # return the max budget allocate as the cap
    # if fits the new budget
    if surplus <= 0: return grantsArray[0]

    index = 0
    while index < N - 1:
        # adjust the new cap by modifying the current
        # overflowing budget to the next lower budget
        # i.e. -> 
        # [6, 4, 2], 3 -> 
        # [4, 4, 2], 3 - >
        # [2, 2, 2], 3 => since there's no lesser budget 
        
        surplus -= (index + 1) * (grantsArray[index] - grantsArray[index + 1])

        # after 2 => [0, 0, 0], 3 and surplus become -3
        # which is the reason we appended 0 (line 4)
        if surplus <= 0:
            break

        index += 1
    

    return grantsArray[index + 1] + abs(surplus)/float(index + 1)


grantsArray = [2, 4, 6]
newBudget = 3
print(find_grants_cap(grantsArray, newBudget))
  
  
  