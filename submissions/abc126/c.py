N, K = map(int, input().split())
lopFlg = True
ansLst = 0
ans = 0
for i in range(1, N + 1):
    tmp = i * 2
    cnt = 1
    while True:
        if i >= K:
            ans += 1
            break
        if K > tmp:
            tmp = tmp * 2
            cnt += 1
        else:
            ans += float(1 / (2 ** cnt))
            break

ans = 1 / N * ans
print(ans)
