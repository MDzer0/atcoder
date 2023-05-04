A, B, C = map(str, input().split())

tmp = A[len(A) - 1]
tmp1 = B[0]
tmp2 = B[len(B) - 1]
tmp3 = C[0]

if tmp == tmp1 and tmp2 == tmp3:
    print('YES')
else:
    print('NO')
