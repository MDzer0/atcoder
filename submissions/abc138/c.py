from heapq import heappush, heappop

N = int(input())
vLst = list(map(int, input().split()))
v = []
for i in range(N):
    heappush(v, vLst[i])

ans = 0
for i in range(N - 1):
    tmp1 = heappop(v)
    tmp2 = heappop(v)
    ans = float((tmp1 + tmp2) / 2)
    heappush(v, ans)

print(v[0])
