from bisect import bisect_right as right
INF = 10 ** 18

def data1():
    half = N // 2
    vwhalf = [[0, 0] for _ in range(1 << half)]
    for i in range(1 << half):
        tmpv, tmpw = 0, 0
        for j in range(half):
            if i >> j & 1:
                tmpv += vw[j][0]
                tmpw += vw[j][1]
        vwhalf[i][0] = tmpv
        vwhalf[i][1] = tmpw
    vwhalf.sort(key=lambda x: x[0], reverse=True)
    vwhalf.sort(key=lambda x: x[1])

    cnt = 0
    v = []
    w = []
    for i in range(1, len(vwhalf)):
        if vwhalf[cnt][1] <= vwhalf[i][1] and \
                vwhalf[cnt][0] >= vwhalf[i][0]:
            vwhalf[i][0] = vwhalf[cnt][0]
        cnt += 1

    for i in range(1 << half):
        v.append(vwhalf[i][0])
        w.append(vwhalf[i][1])

    ans = 0
    for i in range(1 << (N - half)):
        tmpv, tmpw = 0, 0
        for j in range(N - half):
            if i >> j & 1:
                tmpv += vw[half + j][0]
                tmpw += vw[half + j][1]
        if tmpw > W:
            continue
        index = right(w, W - tmpw) - 1
        ans = max(ans, v[index] + tmpv)

    print(ans)
    exit()

def data2():
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W):
            if j - vw[i][1] + 1 >= 0:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i][j - vw[i][1] + 1] + vw[i][0])
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1])
    print(dp[N][W])
    exit()

def data3():
    dp = [[INF] * (maxv * N + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(maxv * N + 1):
            if dp[i][j] == INF: continue
            if dp[i][j] + vw[i][1] <= W:
                dp[i + 1][j + vw[i][0]] = min(dp[i][j + vw[i][0]], dp[i][j] + vw[i][1])
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    ans = 0
    for i in range(maxv * N + 1):
        if dp[N][i] != INF:
            ans = i
    print(ans)
    exit()

N, W = map(int, input().split())
vw = [list(map(int, input().split())) for _ in range(N)]
maxw = 0
maxv = 0

for i in vw:
    if maxw <= i[1]:
        maxw = i[1]
    if maxv <= i[0]:
        maxv = i[0]

if N <= 30:
    data1()
if maxw <= 1000:
    data2()
else:
    data3()
