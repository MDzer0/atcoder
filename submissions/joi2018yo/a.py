nlist = list(map(int, input().split()))
a, b = divmod(nlist[0], nlist[1])
if b != 0:
    a += 1
tmp1 = nlist[2] * a

c, d = divmod(nlist[0], nlist[3])
if d != 0:
    c += 1
tmp2 = nlist[4] * c
print(min(tmp1, tmp2))
