import math
from decimal import Decimal

x, y, r = map(Decimal, input().split())
left = math.ceil(x - r)
right = math.floor(x + r)

ans = 0
for i in range(left, right + 1):
	t = r ** 2 - (x - i) ** 2
	tq = t.sqrt()
	top = math.floor(y + tq)
	bottom = math.ceil(y -tq)
	ans += (top - bottom) + 1
print(ans)
