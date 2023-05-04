import sys
N1, N2, N3, N4 = map(str, input().split())
tmp = N1 + N2 + N3 + N4

for i in '1974':
    if tmp.count(i) != 1:
        print('NO')
        sys.exit()

print('YES')
