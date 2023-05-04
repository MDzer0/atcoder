abcd = list(map(int, input().split()))

for i in range(2 ** 4):
    cmp1 = 0
    cmp2 = 0
    for j in range(4):
        if i >> j & 1:
            cmp1 += abcd[j]
        else:
            cmp2 += abcd[j]
    if cmp1 == cmp2:
        print('Yes')
        exit()

print('No')
