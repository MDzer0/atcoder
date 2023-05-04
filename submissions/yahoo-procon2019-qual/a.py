import sys
N, K = map(int, input().split())

if N % 2 == 0:
    if K <= (N // 2):
        print('YES')
    else:
        print('NO')
else:
    if K <= (N // 2) + 1:
        print('YES')
    else:
        print('NO')
