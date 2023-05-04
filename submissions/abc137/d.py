import heapq
import sys

N, M = map(int, input().split())
tmp = [[] for _ in range(M + 1)]
for i in range(N):
    a, b = map(int, input().split())
    if M >= a:
        tmp[M - a].append(b)
ans = []
for i in range(M + 1):
    for j in tmp[i]:
        heapq.heappush(ans, j)
        if len(ans) > i + 1:
            heapq.heappop(ans)

print(sum(ans))
