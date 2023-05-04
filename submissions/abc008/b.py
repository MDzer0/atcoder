import sys
import collections

N = int(input())
sLst = list(input() for i in range(N))
ansLst = collections.Counter(sLst)
print(ansLst.most_common()[0][0])
