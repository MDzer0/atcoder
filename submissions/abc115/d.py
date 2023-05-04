def dfs(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    if x <= sou[n - 1] + 1:
        return dfs(n - 1, x - 1)
    else:
        return pcnt[n - 1] + 1 + dfs(n - 1, x - 2 - sou[n - 1])

N, X = map(int, input().split())
sou = [1]
pcnt = [1]

for i in range(N):
    sou.append(sou[i] * 2 + 3)
    pcnt.append(pcnt[i] * 2 + 1)

print(dfs(N, X))
