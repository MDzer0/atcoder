N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(N - 4):
    for j in range(i + 1, N - 3):
        for k in range(j + 1, N - 2):
            for l in range(k + 1, N - 1):
                for m in range(l + 1, N):
                    if A[i] + A[j] + A[k] + A[l] + A[m] == 1000:
                        ans += 1

print(ans)
