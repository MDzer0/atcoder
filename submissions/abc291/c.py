from collections import defaultdict

d = defaultdict(int)
N = int(input())
S = list(input())

tmp = [0, 0]
d[(0, 0)] += 1

for i in S:
    if i == 'R':
        tmp[0] += 1
    elif i == 'L':
        tmp[0] -= 1
    elif i == 'U':
        tmp[1] += 1
    else:
        tmp[1] -= 1
    d[(tmp[0], tmp[1])] += 1

keyList = sorted(d.values(), reverse=True)
if keyList[0] != 1:
    print('Yes')
else:
    print('No')
