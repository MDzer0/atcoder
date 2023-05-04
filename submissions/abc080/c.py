import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
flist = [list(map(int, input().split())) for _ in range(N)]
plist = [list(map(int, input().split())) for _ in range(N)]
alist = [0] * 10
def dfs(i, v, ans):
    if v == 10:
        tmp = 0
        if alist.count(1) == 0:
            return ans
        for j in range(N):
            cnt = 0
            for k in range(10):
                if alist[k] == 1 and flist[j][k] == 1:
                   cnt += 1
            tmp += plist[j][cnt]

        ans = max(ans, tmp)
        return ans

    alist[i] = 1
    ans = dfs(i + 1, v + 1, ans)
    alist[i] = 0
    ans = dfs(i + 1, v + 1, ans)
    return ans

print(dfs(0, 0, -10 ** 9 - 1))
