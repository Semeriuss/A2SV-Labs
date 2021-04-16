#!/bin/python3

import math
import os
import random
import re
import sys

# Merge Sort O(nlogn)
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
        

# Complete the findMedian function below.
def findMedian(arr):
    
    #O(1)
    mid = len(arr)//2
    
    #O(nlogn)
    sortedArray = mergeSort(arr) 
    
    #O(n)
    result = sortedArray[mid]   
    
    # O(nlogn)
    print(sortedArray)
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # arr = list(map(int, input().rstrip().split()))
    # fptr.write(str(result) + '\n')
    # fptr.close()

    arr = [1,3,5,6,7,2,4]
    print("The Median value is: ", findMedian(arr))

