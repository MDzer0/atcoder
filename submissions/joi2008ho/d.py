def main():
    n, m = map(int, input().split())
    stones = [[] for _ in range(n)]
    kk = []
    INF = 10**9
    for i in range(n):
        k, *a = map(int, input().split())
        for j in range(k):
            stones[i].append((a[2*j], a[2*j+1]))
        kk.append(k)

    dp1 = [[0]*(m+1) for _ in range(kk[0])]
    dp2 = [[INF]*(m+1) for _ in range(kk[1])]
    if m>0:
        for i in range(kk[1]):
            dp2[i][1] = 0

    for i in range(n-1):
        dp0, dp1 = dp1, dp2
        if i<n-2:
            dp2 = [[INF]*(m+1) for _ in range(kk[i+2])]
        for j in range(kk[i]):
            for k in range(kk[i+1]):
                for l in range(m+1):
                    tmp = dp0[j][l]+(stones[i+1][k][1]+stones[i][j][1])*abs(stones[i+1][k][0]-stones[i][j][0])
                    if dp1[k][l] > tmp:
                        dp1[k][l] = tmp
            if i==n-2:
                continue
            for k in range(kk[i+2]):
                for l in range(m):
                    tmp = dp0[j][l]+(stones[i+2][k][1]+stones[i][j][1])*abs(stones[i+2][k][0]-stones[i][j][0])
                    if dp2[k][l+1] > tmp:
                        dp2[k][l+1] = tmp
    ans = INF
    for i in range(kk[-1]):
        for j in range(m+1):
            if ans > dp1[i][j]:
                ans = dp1[i][j]
    for i in range(kk[-2]):
        for j in range(m):
            if ans > dp0[i][j]:
                ans = dp0[i][j]
    print(ans)

if __name__ == "__main__":
    main()
