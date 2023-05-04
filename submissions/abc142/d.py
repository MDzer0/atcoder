import sys
from fractions import gcd
A, B = map(int, input().split())

glst = []
tmp = gcd(A, B)
for i in range(1, int(tmp ** 0.5) + 1):
    if tmp % i == 0:
        glst.append(i)
        if i != tmp // i:
            glst.append(tmp // i)

glst.sort()
cnt = 0
for i in range(1, len(glst) + 1):
    cntF = True
    for j in range(i + 1, len(glst) + 1):
        if gcd(glst[-i], glst[-j]) != 1:
            cntF = False
            break

    if cntF:
        cnt += 1

print(cnt)
