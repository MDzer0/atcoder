import sys

N = int(input())
ans = 'No'
for i in range(1, 10):
    for j in range(1, 10):
        tmp = i * j
        if tmp == N:
            print('Yes')
            sys.exit()

print('No')
