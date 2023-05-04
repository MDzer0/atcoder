x, y = map(int, input().split())

alist = [1, 3, 5, 7, 8, 10, 12]
blist = [4, 6, 9, 11]
clist = [2]

xg = ''
yg = ''

for i in alist:
    if i == x:
        xg = 'A'

    if i == y:
        yg = 'A'

for i in blist:
    if i == x:
        xg = 'B'

    if i == y:
        yg = 'B'

for i in clist:
    if i == x:
        xg = 'C'

    if i == y:
        yg = 'C'

if xg == yg:
    print('Yes')
else:
    print('No')
