def mergeSort(arr):
    if(len(arr)>1):
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while(i<len(left) and j<len(right)):
            if(left[i] < right[j]):
                arr[k] = left[i]
                i+=1
                k+=1

            else: 
                arr[k] = right[j]
                j+=1
                k+=1
        
        while(i<len(left)):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while(j<len(right)):
            arr[k] = right[j]
            j+=1
            k+=1

    return arr

def intersection(lst1, lst2):
    i = j = 0

    ls1 = mergeSort(lst1) if len(lst1) < len(lst2) else mergeSort(lst2)
    ls2 = mergeSort(lst1) if len(lst1) > len(lst2) else mergeSort(lst2)

    print(ls1, ls2)
    lst = []
    
    while(i<len(ls1) and j<len(ls2)):
        # print(i,ls1[i], "  ---  ",j, ls2[j])
        if(ls1[i] == ls2[j]):
            lst.append(ls1[i]) if i==0 or ls1[i] != lst[-1] else lst
            i+=1
            j+=1
        elif(ls1[i] < ls2[j]):
            i+=1
        else:
            j+=1    

    return lst

lst1 = [3,1,2]
lst2 = [1,3]

arr2 = [4,4,9,5]
arr1 = [9,4,9,8,4]

arr3 = [1,2,2,1]
arr4 = [2,2]

print(intersection(arr3, arr4))
