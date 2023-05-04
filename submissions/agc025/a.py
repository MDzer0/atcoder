N = int(input())
A = str(N - 1)
B = '1'
ans = 10 ** 9
for i in range(1, (N // 2) + 1):
    tmpa = list(map(int, A))
    tmpb = list(map(int, B))
    tmp = sum(tmpa) + sum(tmpb)
    ans = min(ans, tmp)
    A = str(N - i - 1)
    B = str(i + 1)

print(ans)
