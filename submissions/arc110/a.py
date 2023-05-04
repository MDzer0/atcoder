from math import gcd
N = int(input())
tmp = 1
for i in range(N, 1, -1):
    tmp = (tmp * i) // gcd(tmp, i)
print(tmp + 1)
