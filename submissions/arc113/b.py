A, B, C = map(int, input().split())
tmp = pow(B, C, 10 ** 100)
if tmp == 0:
    tmp = B
ans = pow(A, tmp, 10 ** 100)
print(ans % 10)
