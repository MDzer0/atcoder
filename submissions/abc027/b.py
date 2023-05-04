import sys
from itertools import accumulate

N = int(input())
aLst = list(map(int, input().split()))
total = sum(aLst)

if total % N:
    print(-1)
    sys.exit()

a1Lst = list(accumulate(aLst))
avr = total // N
print(sum(a1Lst[i] != (i + 1) * avr for i in range(N)))
