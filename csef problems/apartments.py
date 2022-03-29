import heapq
def solve(applicantsize, apartmentsize, diff):
    heapq.heapify(applicantsize)
    heapq.heapify(apartmentsize)
    count = 0
    while applicantsize and apartmentsize:
        applicant, apartment = heapq.heappop(applicantsize), heapq.heappop(apartmentsize)
        if abs(applicant - apartment) <= diff:
            count += 1
        else:
            if apartment > applicant:
                heapq.heappush(apartmentsize, apartment)
            else:
                heapq.heappush(applicantsize, applicant)
    return count

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    applicantsize = list(map(int, input().split()))
    apartmentsize = list(map(int, input().split()))
    print(solve(applicantsize, apartmentsize, k))