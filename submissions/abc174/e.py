import math
N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
l = 0
r = a[-1] + 1

while r - l > 1:
    mid = (r + l) // 2
    cnt = 0
    for i in a:
        cnt += (i - 1) // mid
    if cnt <= K:
        r = mid
    else:
        l = mid
print(r)
