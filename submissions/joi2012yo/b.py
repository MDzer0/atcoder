N = int(input())
ans = [[0, i] for i in range(1, N + 1)]
for i in range((N * (N - 1) // 2)):
    a, b, c, d = map(int, input().split())
    if c > d:
        ans[a - 1][0] += 3
    elif d > c:
        ans[b - 1][0] += 3
    else:
        ans[a - 1][0] += 1
        ans[b - 1][0] += 1
ans.sort(key=lambda x:x[0], reverse=True)

tmp = 0
cnt = 0
index = 0
juni = [0] * N
for i in range(N):
    if ans[i][0] > tmp:
        tmp = ans[i][0]
        index += 1
        juni[ans[i][1] - 1] = index
    elif ans[i][0] == tmp:
        cnt += 1
        juni[ans[i][1] - 1] = index
    else:
        tmp = ans[i][0]
        index += cnt + 1
        cnt = 0
        juni[ans[i][1] - 1] = index

for i in juni:
    print(i)
