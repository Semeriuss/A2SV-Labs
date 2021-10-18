def find_missing_number(nums):
    for num in set(range(len(nums)+1))-set(nums):
        return num


tests = [[3,0,1],[0,1],[9,6,4,2,3,5,7,0,1],[0]]
for test in tests:
    print(find_missing_number(test))
        
