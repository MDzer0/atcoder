N = int(input())
m, d = divmod(N, 2)
gcnt = m
kcnt = m
if d != 0:
    kcnt += 1

print(3 * kcnt - gcnt * 2)
