import itertools
N = int(input())
x = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans = max(ans, ((x[j][0] - x[i][0]) ** 2 + (x[j][1] - x[i][1]) ** 2) ** 0.5)

print(ans)
