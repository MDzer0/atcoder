N, K = map(int, input().split())
A = list(map(int, input().split()))
R = [0] * N
ruiseki = [0] * (N + 1)
for i in range(N):
    ruiseki[i + 1] = ruiseki[i] + A[i]

ans = 0
for i in range(N):
    down = i
    up = N + 1
    while up - down > 1:
        mid = (up + down) // 2
        if ruiseki[mid] - ruiseki[i] > K:
            up = mid
        else:
            down = mid
    ans += down - i

print(ans)
