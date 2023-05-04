N = int(input())
A = list(map(int, input().split()))
xor = A[0]
for i in range(1, N):
    xor = xor ^ A[i]
if xor == 0:
    print('Second')
else:
    print('First')
