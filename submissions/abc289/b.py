from collections import deque

N, M = map(int, input().split())
p = list(map(int, input().split()))
reten = [0] * N
for i in range(M):
    reten[p[i]] = 1

ans = []
d = deque()
for i in range(1, N):
    if reten[i] == 1:
        d.append(i)
    else:
        d.append(i)
        while d:
            ans.append(d.pop())
d.append(N)
while d:
    ans.append(d.pop())
print(*ans)
