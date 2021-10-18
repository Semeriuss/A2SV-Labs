def relativeSortArray(arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: List[int]
    """
    
    count = [0 for _ in range(1001)]

    for num in arr1:
        count[num] += 1

    for i, num in enumerate(arr2):
        while(count[num] > 0):
            arr1[i] = num
            count[num] -= 1

    
    for j in range(len(count)):
        while(count[j] > 0):
            arr1[count[j]] += 1
            count[j] -= 1

    return arr1

tests = [([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6], [2,2,2,1,4,3,3,9,6,7,19]),
         ([28,6,22,8,44,17], [22,28,8,6], [22,28,8,6,17,44])]

for test in tests:
    arr1, arr2, expected = test
    actual = relativeSortArray(arr1, arr2)
    print(actual == expected, actual, expected)

def relativeSortArray(arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: List[int]
    """

    countMap = dict()
    for num in arr1:
        countMap[n] = countMap.get(n) + 1

    for i, num in enumerate(arr2):
        for j in range(countMap.get(num)):
            arr1[i] = num

    return arr1


##for test in tests:
##    arr1, arr2, expected = test
##    actual = relativeSortArray(arr1, arr2)
##    print(actual == expected, actual, expected)
