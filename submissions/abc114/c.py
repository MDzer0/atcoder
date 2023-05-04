N = int(input())

def dfs(n):
    if N < int(n):
        return 0

    ansB = True
    for i in '753':
        if n.count(i) == 0:
            ansB = False
            break
    ans = 0
    if ansB:
        ans = 1

    for i in '753':
        ans += dfs(n + i)
    return ans

print(dfs('0'))
