A = list(map(int, input().split()))
x = 2 * A[1] - A[0] - A[2]
k = max(0, (1 - x) // 2)
ans = x + 3 * k
print(ans)
