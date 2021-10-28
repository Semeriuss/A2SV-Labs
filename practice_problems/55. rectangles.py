import sys

input = sys.stdin.readline
n, m = tuple(list(map(int, input().split())))

table = []
for i in range(n):
    table.append(list(map(int, input().split())))

def countNonEmptySet(matrix):
    count = 0
    for row in range(len(matrix)):
        row_zero_count, row_one_count = 0, 0
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                row_zero_count += 1 
            else:
                row_one_count += 1

        count += pow(2, row_zero_count) - 1 + pow(2, row_one_count) - 1

    for col in range(len(matrix[0])):
        col_zero_count, col_one_count = 0, 0
        for row in range(len(matrix)):
            if matrix[row][col] == 0:
                col_zero_count += 1
            else:
                col_one_count += 1
        count += pow(2, col_zero_count) - col_zero_count - 1 + pow(2, col_one_count) - col_one_count - 1

    return count

   

print(countNonEmptySet(table))

