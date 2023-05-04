N = int(input())
s = input()

aCnt = s.count('R')
bCnt = s.count('B')

if aCnt > bCnt:
    print('Yes')
else:
    print('No')
