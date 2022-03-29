from bisect import bisect_right
def solve(tickets, customers):
    tickets.sort()
    check = [False]*len(tickets)
    for customer in customers:
        right_index = bisect_right(tickets, customer)
        if not right_index:
            print(-1)
            continue
        if right_index == len(tickets) and check[right_index - 1] == False:
            print(tickets[right_index - 1])
            check[right_index - 1] = True
        else:
            right_index -= 1
            while right_index >= 0 and check[right_index] == True:
                right_index -= 1
            if right_index >= 0:
                print(tickets[right_index])
                check[right_index] = True
            else:
                print(-1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    tickets = list(map(int, input().split()))
    customers = list(map(int, input().split()))
    solve(tickets, customers)