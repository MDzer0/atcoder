from collections import defaultdict
N = int(input())
d = defaultdict(str)
for i in range(N):
    a, b = input().split()
    d[a] = b

ans = ''
M = int(input())
for i in range(M):
    tmp = input()
    if d[tmp]:
        ans += d[tmp]
    else:
        ans += tmp

print(ans)
