from fractions import gcd
N = int(input())
t = list(int(input()) for _ in range(N))
tmp = gcd(0, t[0])
ans = tmp
for i in range(1, N):
    l = ans
    tmp = gcd(ans, t[i])
    ans = (l * t[i]) // tmp

print(ans)
