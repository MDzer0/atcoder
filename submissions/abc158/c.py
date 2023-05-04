import math
A, B = map(int, input().split())
tmpa = math.floor(A / 0.08)
tmpb = math.floor(B / 0.1)
alst = []
blst = []

indexa = 0
while True:
    tmp = math.floor((tmpa + indexa) * 0.08)
    if tmp == A:
        alst.append(tmpa + indexa)
        indexa += 1
    elif tmp > A:
        break
    else:
        indexa += 1

indexb = 0
while True:
    tmp = math.floor((tmpb + indexb) * 0.1)
    if tmp == B:
        blst.append(tmpb + indexb)
        indexb += 1
    elif tmp > B:
        break
    else:
        indexb += 1
ans = -1
alst.sort()
blst.sort()
for i in alst:
    if blst.count(i) >= 1:
        ans = i
        break

print(ans)
