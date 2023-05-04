N = int(input())
m = [list(map(float, input().split())) for _ in range(N)]
ans = [0] * 6
for i in range(N):
    if m[i][0] >= 35:
        ans[0] += 1
    elif m[i][0] >= 30:
        ans[1] += 1
    elif m[i][0] >= 25:
        ans[2] += 1

    if m[i][1] >= 25:
        ans[3] += 1
    elif m[i][1] < 0 and m[i][0] >= 0:
        ans[4] += 1
    elif m[i][1] < 0:
        ans[5] += 1
print(*ans)
