def dfs(cnt):
    global ans
    if cnt == N:
        onF = True
        for i in range(M):
            tmp = 0
            for j in range(ks[i][0]):
                if bit[ks[i][j + 1] - 1] == 1:
                    tmp += 1
            if tmp % 2 != p[i]:
                onF = False
                break
        if onF:
            ans += 1
        return
    for i in range(2):
        bit[cnt] = i
        dfs(cnt + 1)


N, M = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))
bit = [0] * N
ans = 0
dfs(0)
print(ans)
