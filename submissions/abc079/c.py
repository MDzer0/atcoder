import sys
from collections import defaultdict
a = input()
alst = [0, 1]
blst = [0, 1]
clst = [0, 1]
ans = ''
for i in alst:
    for j in blst:
        for k in clst:
            tmp = 0
            ans = ''
            if i == 0:
                tmp = int(a[0]) + int(a[1])
                ans = a[0] + '+' + a[1]
            else:
                tmp = int(a[0]) - int(a[1])
                ans = a[0] + '-' + a[1]
            if j == 0:
                tmp = tmp + int(a[2])
                ans = ans + '+' + a[2]
            else:
                tmp = tmp - int(a[2])
                ans = ans + '-' + a[2]
            if k == 0:
                tmp = tmp + int(a[3])
                ans = ans + '+' + a[3]
            else:
                tmp = tmp - int(a[3])
                ans = ans + '-' + a[3]
            if tmp == 7:
                print(ans + '=7')
                sys.exit()
