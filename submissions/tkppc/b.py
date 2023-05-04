N = int(input())
ans = -1
maxA = -1

for i in range(N):
    A = int(input())
    if maxA < A:
        maxA = A
        ans = i + 1

print(ans)
