import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    if not henkoF[n]:
        return

    henkoF[n] = False
    for i in g[n]:
        if i == n: continue

        dfs(i)

    return

N = int(input())
A = list(map(int, input().split()))
maxA = max(A) + 1

g = [[] for _ in range(maxA)]
henkoF = [False] * maxA
ans = 0
for i in range(N):
    if not henkoF[A[i]]:
        henkoF[A[i]] = True
        ans += 1

for i in range(N // 2):
    g[A[i]].append(A[N - i - 1])
    g[A[N - i - 1]].append(A[i])

for i in range(N):
    if henkoF[A[i]]:
        ans -= 1
        dfs(A[i])
print(ans)
