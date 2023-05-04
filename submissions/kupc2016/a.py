N, A, B = map(int, input().split())
ans = 0
for i in range(N):
    t = int(input())
    if t < A or B <= t:
        ans += 1

print(ans)
