N, Q = map(int, input().split())
A = list(map(int, input().split()))
ruiseki = [0] * (N + 1)
for i in range(N):
    ruiseki[i + 1] = ruiseki[i] + A[i]
for i in range(Q):
    l, r = map(int, input().split())
    print(ruiseki[r] - ruiseki[l - 1])
