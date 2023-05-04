h = list(map(int, input().split()))
tmp1 = h[0] * 60 + h[1]
tmp2 = h[2] * 60 + h[3]
ans = tmp2 - tmp1
print(ans - h[4])
