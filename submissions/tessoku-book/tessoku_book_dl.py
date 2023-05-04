import heapq

N, D = map(int, input().split())
X = [None]*N
Y = [None]*N
for i in range(N):
    X[i], Y[i] = list(map(int,input().split()))
ans = 0
Q = []
for i in range(1, D + 1):
    for j in range(N):
        if X[j] == i:
            heapq.heappush(Q, -Y[j])
        else:
            continue
    if len(Q) > 0:
        ans += abs(heapq.heappop(Q))

print(ans)
