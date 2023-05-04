INF = 10 ** 10

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

right = L + 1
left = 0

while right - left > 1:
    mid = (right + left) // 2
    kCnt = 0
    tmp = 0
    for i in range(N):
        if A[i] - tmp >= mid and L - A[i] >= mid:
            kCnt += 1
            tmp = A[i]
    if kCnt < K:
        right = mid
    else:
        left = mid

print(left)
