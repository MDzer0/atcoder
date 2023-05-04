N = int(input())
ans = 10 ** 10
for i in range(13):
    for j in range(10):
        tmp = i * 8 + j * 10
        ebi = (N - tmp) // 26
        if N == tmp + ebi * 26:
            ans = min(ans, i + j)
print(ans)
