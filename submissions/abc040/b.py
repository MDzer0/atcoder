n = int(input())

ansMin = 100001
for i in range(1, n + 1):
    for j in range(1, n + 1):
        tmp = i * j
        if tmp > n:
            break
        ans = abs(i - j) + (n - tmp)
        ansMin = min(ansMin, ans)


print(ansMin)
