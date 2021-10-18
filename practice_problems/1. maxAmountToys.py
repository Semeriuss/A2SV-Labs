
# O(n*n) method
def min(lst):
    key = lst[0]
    for i in lst:
        if(i<key):
            key = i
    return key

def maxToys1(n, k): 
    lst = n
    sum = 0
    count = 0
    
    while(sum<=k):
        sum += min(lst)
        lst.remove(min(lst))
        if(sum<=k):
            count+=1
        

    return count

# O(nlogn) using merge Sort
def mergeSort(arr):
    if(len(arr)>1):
        
        m = len(arr)//2

        l = arr[:m]
        r = arr[m:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while(i<len(l) and j<len(r)):
            if(l[i]<r[j]):
                arr[k]=l[i]
                i+=1
                k+=1
            else:
                arr[k]=r[j]
                j+=1
                k+=1

        while(i<len(l)):
            arr[k] = l[i]
            i+=1
            k+=1

        while(j<len(r)):
            arr[k] = r[j]
            j+=1
            k+=1

    return arr

def maxToys(lstTag, amount):
    lst = mergeSort(lstTag)
    sum = 0
    count = 0

    for i in lst:
        sum+=i
        print(sum, count)
        if(sum<amount):
            count+=1

    return count


ls = [1,2,3,4]
am = 7
ls2 = [1,12, 5, 111,200, 1000, 10]
am2 = 50

print(maxToys(ls, am))
print(maxToys(ls2, am2))

##lst = [1,5,2,9,0,3,6,7,8,4]
##newlst = mergeSort(lst)
##print(mergeSort(newlst))
