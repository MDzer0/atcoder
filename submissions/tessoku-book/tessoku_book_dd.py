import math

N = int(input())
ans = N // 3
ans += N // 5
ans += N // 7
ans -= N // 15
ans -= N // 21
ans -= N // 35
gcdTmp = math.gcd(3, 5)
gcdTmp = math.gcd(gcdTmp, 7)
tmp = (3 * 5 * 7) // gcdTmp
ans += N // tmp
print(ans)
