n = int(input())
tmp = 2 * n
tmp1 = int(pow(tmp, 0.5))
tmp2 = tmp1 + 1
if tmp1 * tmp2 == tmp:
    print(tmp1)
else:
    print(-1)
