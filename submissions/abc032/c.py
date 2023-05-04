import sys
import bisect

N, K = map(int, input().split())
s = []

endf = False

for i in range(N):
    s.append(int(input()))
    if s[i] == 0:
        endf = True

if endf:
    print(N)
    sys.exit()

ans = 0
l = 0
tmp = 1
for i in range(N):
    tmp *= s[i]
    if tmp <= K:
        ans = max(ans, i - l + 1)
    else:
        tmp //= s[l]
        l += 1

print(ans)
