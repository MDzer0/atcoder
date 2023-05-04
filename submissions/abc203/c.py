N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort()

tmp = AB[0][0]
if K - tmp < 0:
    print(K)
    exit()

ans = tmp
K += AB[0][1] - tmp

for i in range(1, N):
    a, b = AB[i][0], AB[i][1]
    if tmp != a:
        tmp1 = K - (a - tmp)
        if tmp1 < 0:
            print(ans + a - tmp + tmp1)
            exit()
        ans += (a - tmp)
        K += b - (a - tmp)
        tmp = a
    else:
        K += b

print(ans + K)
