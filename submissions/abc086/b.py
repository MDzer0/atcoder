import math
a, b = map(str, input().split())

total = a + b
if math.sqrt(int(total)).is_integer():
    print('Yes')
else:
    print('No')
