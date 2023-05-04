N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(1, 101):
    for j in range(1, 101):
        tmp = 0
        for k in range(N):
            if i <= AB[k][0] and AB[k][0] <= i + K and\
                j <= AB[k][1] and AB[k][1] <= j + K:
                tmp += 1
        ans = max(ans, tmp)
print(ans)
