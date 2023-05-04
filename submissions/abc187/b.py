N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        x1, y1 = xy[i][0], xy[i][1]
        x2, y2 = xy[j][0], xy[j][1]
        if -1 <= (y1 - y2) / (x1 - x2) <= 1:
            ans += 1

print(ans)
