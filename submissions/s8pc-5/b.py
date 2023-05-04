import math

N, M = map(int, input().split())
xyr = [list(map(int, input().split())) for _ in range(N + M)]
ans = 10 ** 10

for i in range(N + M - 1):
    r1 = 0
    if len(xyr[i]) == 3:
        ans = min(ans, xyr[i][2])
        r1 = xyr[i][2]

    for j in range(i + 1, N + M):
        r2 = 0
        if len(xyr[j]) == 3:
            r2 = xyr[j][2]
            ans = min(ans, xyr[j][2])

        if r1 != 0 and r2 != 0: continue
        if r1 == 0 and r2 == 0:
            ans = min(ans, math.sqrt(abs(xyr[i][0] - xyr[j][0]) ** 2 +
                                     abs(xyr[i][1] - xyr[j][1]) ** 2) / 2)
        elif r1 == 0:
            ans = min(ans, math.sqrt(abs(xyr[i][0] - xyr[j][0]) ** 2 +
                                     abs(xyr[i][1] - xyr[j][1]) ** 2) - r2)
        else:
            ans = min(ans, math.sqrt(abs(xyr[i][0] - xyr[j][0]) ** 2 +
                                     abs(xyr[i][1] - xyr[j][1]) ** 2) - r1)

print(ans)
