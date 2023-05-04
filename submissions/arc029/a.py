N = int(input())
t = [int(input()) for _ in range(N)]
tlst = [0] * N
ans = 10 ** 10
def dfs(n):
    global ans
    if n == N:
        tmp1, tmp2 = 0, 0
        for i in range(N):
            if tlst[i] == 0:
                tmp1 += t[i]
            else:
                tmp2 += t[i]
        ans = min(ans, max(tmp1, tmp2))
        return

    for i in range(2):
        tlst[n] = i
        dfs(n + 1)

dfs(0)
print(ans)
