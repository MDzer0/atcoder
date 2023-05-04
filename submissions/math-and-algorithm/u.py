import math

n, r = map(int, input().split())
ans = math.factorial(n) // (math.factorial(r) * (math.factorial(n - r)))
print(ans)
