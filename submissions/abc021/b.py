import sys
import collections

N = int(input())
a, b = map(int, input().split())
K = int(input())
pLst = list(map(int, input().split()))
tmp = collections.Counter(pLst)
if pLst.count(a) > 0 or pLst.count(b):
    print('NO')
    sys.exit()

if tmp.most_common()[0][1] > 1:
    print('NO')
else:
    print('YES')

