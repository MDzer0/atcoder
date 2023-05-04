A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V <= W:
    print('NO')
    exit()

tmp = abs(B - A)
k = V - W
if tmp <= k * T:
    print('YES')
else:
    print('NO')
