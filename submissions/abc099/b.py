a, b = map(int, input().split())
ansb = 0
tmp = b - a
for i in range(tmp, 0, -1):
    ansb += i
print(ansb - b)
