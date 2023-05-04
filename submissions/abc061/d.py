INF = 10 ** 18
N, M = map(int, input().split())
abc = []
d = [INF] * N
d[0] = 0
loop = [False] * N

for i in range(M):
    a, b, c = map(int, input().split())
    abc.append([a - 1, b - 1,  -c])

for j in range(N):
    for i in range(M):
        if d[abc[i][1]] > d[abc[i][0]] + abc[i][2]:
            d[abc[i][1]] = d[abc[i][0]] + abc[i][2]
ans = -1 * d[-1]

for i in range(N):
    for j in range(M):
        if d[abc[j][1]] > d[abc[j][0]] + abc[j][2]:
            d[abc[j][1]] = d[abc[j][0]] + abc[j][2]
            loop[abc[j][1]] = True

        if loop[abc[j][0]] == True:
            loop[abc[j][1]] = True

if loop[N - 1]:
    print('inf')
else:
    print(ans)
