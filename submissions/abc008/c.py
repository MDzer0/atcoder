N = int(input())
C = list(int(input()) for _ in range(N))

ans = 0.0
for i in range(N):
    S = 0
    for j in range(N):
        if i != j:
            if C[i] % C[j] == 0:
                S += 1

    if S % 2 == 0:
        ans += (S + 2) / ((2 * S) + 2)
    else:
        ans += 1 / 2

print(ans)
