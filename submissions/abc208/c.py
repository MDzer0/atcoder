N, K = map(int, input().split())
a = [[0, 0, 0] for _ in range(N)]
tmpA = list(map(int, input().split()))

for i in range(N):
    a[i][0] = tmpA[i]
    a[i][1] = i

a.sort()
m, d = divmod(K, N)
for i in range(N):
    if d != 0:
        a[i][2] = m + 1
        d -= 1
    else:
        a[i][2] = m

a.sort(key=lambda x: x[1])
for i in a:
    print(i[2])
