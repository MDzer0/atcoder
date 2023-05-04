N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
MOD = 10 ** 9 + 7

ans = 1
for i in range(N):
    ans *= sum(A[i])
    ans %= MOD
print(ans)
