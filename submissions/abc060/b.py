import sys

A, B, C = map(int, input().split())

for i in range(B):
    if (A * i) % B == C:
        print('YES')
        sys.exit()

print('NO')
