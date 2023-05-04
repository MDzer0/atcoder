P, Q, R = map(int, input().split())
tmp1 = P + Q
tmp2 = R + Q
tmp3 = P + R
ans = min(tmp1, tmp2, tmp3)
print(ans)
