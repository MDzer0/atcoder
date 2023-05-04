from fractions import gcd

N = int(input())
a = list(map(int, input().split()))

def lcm(x, y):
    return (x * y) // gcd(x, y)

tmp = lcm(a[0], a[1])
for i in range(2, N):
    tmp = lcm(tmp, a[i])
tmp -= 1
ans = 0
for i in range(N):
    ans += tmp % a[i]

print(ans)
