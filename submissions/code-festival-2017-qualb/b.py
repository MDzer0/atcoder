import heapq

def heap(h):
    hlst = list(map(int, input().split()))
    for i in hlst:
        heapq.heappush(h, i)
N = int(input())
d = []
heap(d)
M = int(input())
t = []
heap(t)

ans = 'YES'
for j in range(M):
    tmpT = heapq.heappop(t)
    for i in range(N):
        tmpD = heapq.heappop(d)
        if tmpT == tmpD:
            break
        if tmpT < tmpD:
            ans = 'NO'
            break
    if ans == 'NO':
        break

print(ans)
