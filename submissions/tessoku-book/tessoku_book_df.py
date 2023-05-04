N, H, W = map(int, input().split())
xor = 0
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    xor ^= a
    xor ^= b

if xor == 0:
    print('Second')
else:
    print('First')
