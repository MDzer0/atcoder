N = int(input())
a = list(map(int, input().split()))


ttotal = -10 ** 5
for i in range(N):
    maxTotal = -10 ** 5
    index = 0
    for j in range(N):
        total = 0
        if i == j:
            continue
        for k in range(min(i, j), max(i, j) + 1):
            if (k - min(i, j)) % 2 != 0:
                total += a[k]
        if maxTotal < total:
            maxTotal = total
            index = j
    tmp = 0
    for j in range(min(index, i), max(index, i) + 1, 2):
        tmp += a[j]
    if ttotal < tmp:
        ttotal = tmp

print(ttotal)
