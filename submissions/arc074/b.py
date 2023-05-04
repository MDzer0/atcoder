import numpy as np

import heapq
N = int(input())
a = list(map(int, input().split()))
ra = -np.array(a[::-1])

def serchPop(alst):
    h = []
    total = []
    sum = 0
    for i in range(2 * N):
        heapq.heappush(h, alst[i])
        sum += alst[i]
        if i >= N:
            tmp = heapq.heappop(h)
            sum -= tmp

        if i >= N - 1:
            total.append(sum)

    return total

ans = -10 ** 20
ltotal = serchPop(a)
rtotal = serchPop(ra)
for i in range(N + 1):
    ans = max(ans, ltotal[i] + rtotal[N - i])

print(ans)
