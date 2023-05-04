import math
N, T = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in a:
    if ans < i:
        ans += i
    else:
        k = math.ceil((ans - i) / T)
        ans = i + (k * T)
print(ans)
