N, K = map(int, input().split())
S = input()
scount = S.count('1')
tmp = abs(scount - K)
if tmp % 2 == 0:
    print('Yes')
else:
    print('No')
