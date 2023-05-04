import math

K = int(input())
total = 0
for i in range(1, K + 1):
    for j in range(1, K + 1):
        for k in range(1, K + 1):
            total += math.gcd(k, math.gcd(i, j))

print(total)
