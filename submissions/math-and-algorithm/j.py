N = int(input())
tokuten = [[0, 0] for _ in range(N)]

for i in range(N):
    c, p = list(map(int, input().split()))
    tokuten[i][c - 1] = p
ruiseki = [[0, 0] for _ in range(N + 1)]
for i in range(N):
    ruiseki[i + 1][0] += ruiseki[i][0] + tokuten[i][0]
    ruiseki[i + 1][1] += ruiseki[i][1] + tokuten[i][1]

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(ruiseki[r][0] - ruiseki[l - 1][0], ruiseki[r][1] - ruiseki[l - 1][1])
