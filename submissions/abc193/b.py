INF = 10 ** 18
N = int(input())
apx = [list(map(int, input().split())) for _ in range(N)]
ans = INF

for i in apx:
    if i[0] < i[2]:
        ans = min(ans, i[1])

if ans == INF:
    print(-1)
else:
    print(ans)
