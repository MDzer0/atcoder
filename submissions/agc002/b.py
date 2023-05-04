N, M = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(M)]
s = [1] * N
a = [0] * N
a[0] = 1
for i in range(M):
    s[x[i][0] - 1] -= 1
    if a[x[i][0] - 1] == 1:
        a[x[i][1] - 1] = 1
        if s[x[i][0] - 1] == 0:
            a[x[i][0] - 1] = 0
    s[x[i][1] - 1] += 1


print(sum(a))
