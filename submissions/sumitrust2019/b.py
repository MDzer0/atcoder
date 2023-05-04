import math

N = int(input())
tmp1 = math.ceil(N / 1.08)
tmp2 = int(tmp1 * 1.08)

if N == tmp2:
    print(tmp1)
else:
    print(':(')
