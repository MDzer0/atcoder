N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(x):
    tmp = 0
    for i in range(N):
        tmp += x // A[i]
    if tmp >= K:
        return True
    else:
        return False

left = 1
right = 10 ** 9
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
