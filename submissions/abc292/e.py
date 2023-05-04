from collections import deque

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)

d = deque()
ans = 0
for i in range(N):
    check = [0] * N
    check[i] = 1
    d.append(i)

    while d:
        tmp = d.popleft()
        for j in g[tmp]:
            if check[j] == 1:continue
            ans += 1
            check[j] = 1
            d.append(j)
print(ans - M)
