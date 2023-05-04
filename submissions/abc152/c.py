INF = 10 ** 9
N = int(input())
p = list(map(int, input().split()))
cnt = 1
minlst = [INF] * N
minlst[0] = p[0]
for i in range(1, N):
    minlst[i] = min(minlst[i - 1], p[i])

for i in range(1, N):
    if minlst[i] >= p[i]:
        cnt += 1

print(cnt)
