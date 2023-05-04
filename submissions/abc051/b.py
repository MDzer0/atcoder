import sys

K, S = map(int, input().split())

ans = 0
if S == (3 * K):
    ans = 1
    print(ans)
    sys.exit()

for x in range(K + 1):
    for y in range(K + 1):
        z = S - x - y
        if z <= K and z >= 0:
            ans += 1

print(ans)
