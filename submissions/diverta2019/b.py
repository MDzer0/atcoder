R, G, B, N = map(int, input().split())
ans = 0
for i in range(int(N/R) + 1):
    for j in range(int(N/G) + 1):
        tmp = int((R * i) + (G * j))
        if N >= tmp and (N - tmp) % B == 0:
            ans += 1
print(ans)
