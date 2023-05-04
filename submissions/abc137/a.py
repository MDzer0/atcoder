A, B = map(int, input().split())
ans = -1000

tmp1 = A + B
tmp2 = A * B
tmp3 = A - B
print(max(tmp1, tmp2, tmp3))
