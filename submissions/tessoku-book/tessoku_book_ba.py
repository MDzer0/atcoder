import heapq
Q = int(input())
he = []

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(he, query[1])
    elif query[0] == 2:
        print(he[0])
    else:
        heapq.heappop(he)
