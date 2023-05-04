import sys
A, B = map(int, input().split())

AB = A * B
for i in range(3):
    tmp = AB * (i + 1)
    if tmp % 2 != 0:
        print('Yes')
        sys.exit()

print('No')
