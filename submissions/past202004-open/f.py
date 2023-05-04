import heapq

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    AB[i][1] = -AB[i][1]
total = 0
AB.sort(key=lambda x: x[0])
h = []
index = 0
cnt = 0
while cnt <= N - 1:
    if N > index and AB[index][0] <= cnt + 1:
        heapq.heappush(h, AB[index][1])
        index += 1
    else:
        total += heapq.heappop(h)
        cnt += 1
        print(-total)
