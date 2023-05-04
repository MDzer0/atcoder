import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    if n > 3234566667:
        return
    ans.append(n)
    if n % 10 != 0:
        dfs(n * 10 + (n % 10) - 1)
    dfs(n * 10 + (n % 10))
    if n % 10 != 9:
        dfs(n * 10 + (n % 10) + 1)

N = int(input())
ans = []
for i in range(1, 10):
    dfs(i)
ans.sort()
print(ans[N - 1])
