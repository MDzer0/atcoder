N = int(input())
ans = 0
for i in range(N):
    if sum(list(map(int, input().split()))) < 20:
        ans += 1

print(ans)
