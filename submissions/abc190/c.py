N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

ans = 0

for i in range(1 << K):
    check = [0] * 101
    for j in range(K):
        if i >> j & 1:
            check[CD[j][1]] = 1
        else:
            check[CD[j][0]] = 1

    tmp = 0
    for j in AB:
        if check[j[0]] == 1 and check[j[1]] == 1:
            tmp += 1
    ans = max(ans, tmp)

print(ans)
