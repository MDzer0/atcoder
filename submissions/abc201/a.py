A = list(map(int, input().split()))
A.sort()
tmp = A[1] - A[0]
if tmp == A[2] - A[1]:
    print('Yes')
else:
    print('No')
