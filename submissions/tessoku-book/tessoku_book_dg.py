N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
xor = 0

for i in range(N):
    if A[i] % 5 == 0 or A[i] % 5 == 1:
        xor ^= 0
    elif A[i] % 5 == 2 or A[i] % 5 == 3:
        xor ^= 1
    else:
        xor ^= 2

if xor != 0:
    print('First')
else:
    print('Second')
