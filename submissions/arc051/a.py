import math
x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())
ans = ['YES', 'YES']
chkx = [x2, x2, x3, x3]
chky = [y2, y3, y2, y3]
chf = True
for i in range(4):
    if (chkx[i] - x1) ** 2 + (chky[i] - y1) ** 2 > r ** 2:
        chf = False
        break

if chf:
    ans[1] = 'NO'

if x2 <= x1 - r and x1 + r <= x3\
    and y2 <= y1 - r and y1 + r <= y3:
    ans[0] = 'NO'

for i in ans:
    print(i)
