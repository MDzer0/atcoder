p = [input() for _ in range(10)]

for i in range(10):
    cnt = 0
    for j in range(10):
        if p[j][i] == 'o':
            cnt += 1
            break
    if cnt == 0:
        print('No')
        exit()
print('Yes')
