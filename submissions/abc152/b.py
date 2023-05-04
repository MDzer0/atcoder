a, b = map(int, input().split())
tmp1 = str(a) * b
tmp2 = str(b) * a
print(min(tmp1, tmp2))
