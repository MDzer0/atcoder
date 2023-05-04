import sys
from collections import defaultdict
INF = 998244353
N = int(input())
dl = list(map(int, input().split()))
if dl[0] != 0:
    print(0)
    sys.exit()
d = defaultdict(int)

for i in range(N):
    d[dl[i]] += 1

d = sorted(d.items(), key=lambda x: x[0])

if d[0][1] != 1:
    print(0)
    sys.exit()

ans = 1
for i in range(len(d) - 1, 0, -1):
    if d[i][0] - 1 == d[i - 1][0]:
        ans *= (d[i - 1][1] ** d[i][1])
        ans = ans % INF
    else:
        print(0)
        sys.exit()

print(ans)
