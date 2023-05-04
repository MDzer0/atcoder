N = int(input())

ans = 0
for i in range(N):
    p, q = map(int, input().split())
    ans += q / p
print(ans)
