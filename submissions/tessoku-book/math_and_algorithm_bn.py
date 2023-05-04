N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
LR.sort(key=lambda x: (x[1], x[1]))
ans = 1
tmp = LR[0][1]
for i in range(1, N):
    if tmp <= LR[i][0]:
        ans += 1
        tmp = LR[i][1]
print(ans)
