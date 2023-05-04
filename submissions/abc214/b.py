S, T = map(int, input().split())
ans = 0

for i in range(S + 1):
    for j in range(S + 1):
        for k in range(S + 1):
            plus = i + j + k
            seki = i * j * k
            if plus <= S and seki <= T:
                ans += 1
print(ans)
