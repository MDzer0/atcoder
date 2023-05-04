N = int(input())
total = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    ans = max(ans, sum(total[i][0:-1]) + (total[i][-1] * (110 / 900)))

print(ans)
