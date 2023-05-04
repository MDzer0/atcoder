N, D, K = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(D)]
st = [list(map(int, input().split())) for _ in range(K)]

minzoku = [0] * K
ans = [0] * K
for i in range(D):
    for j in range(K):
        if minzoku[j] == 1:
            continue
        if st[j][0] <= st[j][1]:
            if lr[i][0] <= st[j][0] and st[j][0] <= lr[i][1]:
                st[j][0] = lr[i][1]
                if st[j][0] >= st[j][1]:
                    minzoku[j] = 1
        else:
            if lr[i][0] <= st[j][0] and st[j][0] <= lr[i][1]:
                st[j][0] = lr[i][0]
                if st[j][0] <= st[j][1]:
                    minzoku[j] = 1
        ans[j] += 1

for i in ans:
    print(i)
