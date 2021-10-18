'''
Semeriuss
May 21, 2021
'''

#Sort an array containing only three types of values in-place

def sortColors_indexMethod(arr):

    if(len(arr) > 1):
        next_zero = 0
        next_two = len(arr)-1

        i = 0

        while(i <= next_two):
            if arr[i] == 2:
                arr[i], arr[next_two] = arr[next_two], arr[i]
                next_two -= 1
                
                #i isn't incremented since arr[next_two] could possibly be a 2

            elif arr[i] == 0:
                arr[next_zero], arr[i] = arr[i], arr[next_zero]
                next_zero += 1

                i += 1

            else:
                i += 1
    print(arr)

def sortColors_indexMethod2(arr):
    if(len(arr) > 1):
        zero_count = one_count = two_count = 0

        for val in arr:
            if val == 0:
                zero_count += 1
            elif val == 2:
                two_count += 1
            else:
                one_count += 1

        for i in range(len(arr)):
            if i < zero_count:
                arr[i] = 0

            elif i < zero_count + one_count:
                arr[i] = 1

            else:
                arr[i] = 2

    print(arr)



def sortColors_dictMethod(arr):
    vals = { 0: 0, 1 : 0, 2: 0}

    for val in arr:
        vals[val] += 1

    counter = 0
    for k, v in vals.items():
        for j in range(vals[k]):
            arr[counter] = k
            counter += 1

    print(arr)
            

sortColors_dictMethod([2,1,2,0,1,2,2,1,2,1,0,0,1,2,1,1,0,0,0,1])
sortColors_indexMethod([2,1,2,0,1,2,2,1,2,1,0,0,1,2,1,1,0,0,0,1])
sortColors_indexMethod2([2,1,2,0,1,2,2,1,2,1,0,0,1,2,1,1,0,0,0,1])
sortColors_indexMethod2([1,1])
