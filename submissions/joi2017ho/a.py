N, Q, S, T = map(int, input().split())
A = [int(input()) for _ in range(N + 1)]
ans = 0
ruiseki = [0] * (N + 2)
for i in range(1, N + 1):
    ruiseki[i] = A[i] - A[i - 1]
    if A[i] > A[i - 1]:
        ans -= (A[i] - A[i - 1]) * S
    else:
        ans += (A[i - 1] - A[i]) * T

for i in range(Q):
    L, R, X = map(int, input().split())

    if ruiseki[L] > 0:
        ans += S * ruiseki[L]
    else:
        ans += T * ruiseki[L]
    ruiseki[L] += X
    if ruiseki[L] > 0:
        ans -= S * ruiseki[L]
    else:
        ans -= T * ruiseki[L]

    if R < N:
        if ruiseki[R + 1] > 0:
            ans += S * ruiseki[R + 1]
        else:
            ans += T * ruiseki[R + 1]
        ruiseki[R + 1] -= X
        if ruiseki[R + 1] > 0:
            ans -= S * ruiseki[R + 1]
        else:
            ans -= T * ruiseki[R + 1]
    print(ans)
