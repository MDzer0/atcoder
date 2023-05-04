N, R = map(int, input().split())
tmp = 100 * (10 - N)
ans = R
if tmp >= 0:
    ans += tmp

print(ans)
