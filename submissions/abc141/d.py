import heapq
import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    for i in range(M):
        A[0] = A[0] // 2
    print(sum(A))
    sys.exit()
h = []
for i in range(N):
    heapq.heappush(h, -A[i])

for i in range(M):
    tmp = heapq.heappop(h)
    tmp = -(-tmp // 2)
    heapq.heappush(h, tmp)


print(-sum(h))
