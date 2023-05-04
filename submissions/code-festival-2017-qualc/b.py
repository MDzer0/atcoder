import sys
sys.setrecursionlimit(10**7)

N = int(input())
a = list(map(int, input().split()))
b = [0] * N
ans = 0

def dfs(v):
    global ans
    if v == N:
        tmp = 1
        for i in b:
            tmp *= i
        if tmp % 2 == 0:
            ans += 1
        return

    b[v] = a[v] - 1
    dfs(v + 1)
    b[v] = a[v]
    dfs(v + 1)
    b[v] = a[v] + 1
    dfs(v + 1)
    return

dfs(0)
print(ans)
