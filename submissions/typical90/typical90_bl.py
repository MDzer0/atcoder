N, Q = map(int, input().split())
A = list(map(int, input().split()))
ruiseki = [0] * (N + 1)
ans = 0
for i in range(N - 1):
    ruiseki[i + 1] = A[i] - A[i + 1]
    ans += abs(ruiseki[i + 1])

for i in range(Q):
    L, R, V = map(int, input().split())
    mae = abs(ruiseki[L - 1]) + abs(ruiseki[R])
    if L > 1:
        ruiseki[L - 1] -= V
    if R < N:
        ruiseki[R] += V
    ato = abs(ruiseki[L - 1]) + abs(ruiseki[R])
    ans += (ato - mae)
    print(ans)
