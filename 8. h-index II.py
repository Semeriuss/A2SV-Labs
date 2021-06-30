def h_index_helper(arr):
    mid = len(arr)//2
    print(mid)
    if arr[mid] == len(arr)-mid:
        return arr[mid]

    elif arr[mid] < len(arr)-mid:
        return h_index_helper(arr[mid:])

    elif arr[mid] > len(arr)-mid:
        return h_index_helper(arr[:mid])

    else:
        print("hi")
        
def h_index_rec(citations):
    if (n:=len(citations)) < 2:
        return n
    return h_index_helper(citations)

def h_index_iter(citations):
    ln = len(citations)
    mid = ln//2
    i = 0
    count = 0
    
    if ln<2: return ln
    while count < ln:
        if citations[mid] == ln-mid:
            return count
        elif citations[mid] < ln-mid:
            mid += (ln-mid)//2
            count = citations[mid]
        elif citations[mid] > ln-mid:
            mid -= 1
            count -= 1
        else:
            print("hhjh")
        i+=1
    return count

def h_index_iter(arr):
    ln = len(arr)
    mid = ln//2
    count = 0
    if len(set(arr)) == 1 and arr[0] == 0:
        return 0        
    if ln < 2:
        return ln
    if arr[mid] < ln-mid:
        count = arr[mid]
        while arr[mid] <= ln-mid:
            mid += 1
            if arr[mid] > ln-mid:
                break
            elif arr[mid] == ln-mid:
                count += 1
                break
        return count

    elif arr[mid] > ln-mid:
        count = ln-mid if arr[mid] <= ln else 1
        while arr[mid] >= ln-mid:
            mid -= 1
            if arr[mid] < ln-mid:
                break
            elif arr[mid] == ln-mid:
                count += 1
            else:
                count += 1
                break
        return count
    else:
        count = ln-mid
        return count
        
        
    
    

test = [0,1,2,4,4,4,4,5,5,7,8,9] #5
test0 = [1,4,7,9] #3
test1 = [1,1,3] #1
test2 = [100] #1
test3 = [0] #0
test4 = [1,1,3,3,4,4] #3
test5 = [1,1,4,4] #1
test6 = [0,0] #0
test7 = [1,2] #1
test8 = [11,15] #2
test9 = [0,0,4,4] #2
test10 = [0, 1, 3, 5, 6] #3
test11 = [1,2,100] #2
test12 = [100,100] #2
test13 = [0,1] #1



tests = [test, test0, test1,
         test2, test3, test4,
         test5, test6, test7,
         test8, test9, test10,
         test11, test12, test13]
##
##for test in tests:
##    print(h_index_iter(test))
print(h_index_iter(test13))
