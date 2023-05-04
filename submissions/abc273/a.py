def dfs(k):
    if k == 0:
        return 1
    return k * dfs(k - 1)

N = int(input())
print(dfs(N))
