N, K, M, R = map(int, input().split())
S = list(int(input()) for _ in range(N - 1))

S.sort(reverse=True)
total = S[:K - 1]
ans = (R * K) - (sum(S[:K - 1]))

if ans > M:
    print(-1)
else:
    if (R * K) - (sum(S[:K])) <= 0:
        print(0)
    else:
        print(ans)
