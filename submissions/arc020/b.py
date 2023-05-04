n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 10 ** 10

for i in range(1, 11):
    for j in range(1, 11):
        if i == j: continue
        diffCnt = 0
        for k in range(0, n, 2):
            if a[k] != i:
                diffCnt += 1
            if k + 1 < n and a[k + 1] != j:
                diffCnt += 1
        ans = min(ans, diffCnt * c)
print(ans)
