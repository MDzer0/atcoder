import math
ABC = list(map(int, input().split()))
abcG = math.gcd(ABC[0], ABC[1])
abcG = math.gcd(abcG, ABC[2])

ans = 0
for i in range(3):
    ans += ABC[i] // abcG
    ans -=1
print(ans)
