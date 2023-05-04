import sys

X = int(input())
tmp1 = X // 100
tmp2 = X % 100
ans = 1

if X < 100:
    print(0)
    sys.exit()
if tmp1 == 0:
    print(ans)
    sys.exit()

for i in range(5, 0, -1):
    t1 = tmp2 // i
    t2 = tmp2 % i
    tmp2 = t2
    tmp1 -= t1
    if tmp1 < 0:
        ans = 0
        break

if t2 != 0:
    ans = 0

print(ans)
