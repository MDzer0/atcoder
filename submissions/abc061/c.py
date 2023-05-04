import sys
from collections import defaultdict

N, K = map(int, input().split())
ans = [0] * ((10 ** 5) + 1)

for i in range(N):
    a, b = map(int, input().split())
    ans[a] += b
cnt = 0
for i in range(10 ** 5 + 1):
    cnt += ans[i]
    if K <= cnt:
        print(i)
        sys.exit()
