def mergeSort(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        
        left = arr[:mid]
        right = arr[mid:]
        
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while(i<len(left) and j<len(right)):
            if(left[i]<right[j]):
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
def h_index(arr):
    arr = mergeSort(arr)
    
    count = 0
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            continue
        elif arr[i] > len(arr):
            count += 1
        elif arr[i]  < len(arr):
            count += 1
            if arr[i] == len(arr)-i :
                return arr[i]
            elif arr[i] < len(arr)-i:
                count-=1
        else:
            count += 1
    return count  



lst = [0,1,2,4,4,4,4,5,5,7,8,9] #5
lst0 = [1,7,9,4] #[1,4,7,9] # 3
lst1 = [1,3,1] #[1,1,3] #1
lst2 = [100] #1
lst3 = [0] #0
lst4 = [1,1,3,3,4,4] #3
lst5 = [1,1,4,4] #1
lst6 = [0,0] #0
lst7 = [1,2] #1
lst8 = [11,15] # 2
lst9 = [4,4,0,0] # 2
print(h_index(lst0))
