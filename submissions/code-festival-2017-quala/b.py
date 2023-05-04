N, M, K = map(int, input().split())
ans = 'No'
for i in range(N + 1):
    for j in range(M + 1):
        tmp = j * (N - i) + i * (M - j)
        if tmp == K:
            ans = 'Yes'
            break

print(ans)
