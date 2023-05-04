N, K = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += i
    if ans == N:
        ans = N
        break
    else:
        if ans > N:
            ans = 2 * N - ans

print(ans)
