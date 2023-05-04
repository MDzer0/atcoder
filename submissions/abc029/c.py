N = int(input())
moji = ['a', 'b', 'c']
mlist = [0] * N
def dfs(n):
    if n < N:
        mlist[n] = 0
    else:
        tmpA = ''
        for i in range(N):
            if mlist[i] == 0:
                tmpA += moji[0]
            elif mlist[i] == 1:
                tmpA += moji[1]
            else:
                tmpA += moji[2]
        print(tmpA)
        return
    dfs(n + 1)
    mlist[n] = 1
    dfs(n + 1)
    mlist[n] = 2
    dfs(n + 1)

dfs(0)
