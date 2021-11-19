
def timeToBuy(tickets, k):
    time = 0
    i = 0
    while tickets[k] != 0:
        if i >= len(tickets):
            i = 0

        if tickets[i] == 0 and i == k:
            break

        if tickets[i] > 0:
            tickets[i] -= 1
            time += 1
            i += 1
        
        elif tickets[i] == 0:
            i += 1

    return time

tickets = [2,3,2]
k = 2

tickets = [5,1,1,1]
k = 0

tickets = [1,3,1,1]
k = 1
print(timeToBuy(tickets, k))