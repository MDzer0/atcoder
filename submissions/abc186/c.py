N = int(input())
cnt = 0

for i in range(1, N + 1):
    if str(i).count('7') >= 1:
        continue
    else:
        tmp = str(format(i, 'o'))
        if tmp.count('7') >= 1:
            continue
    cnt += 1

print(cnt)
