N, v, u, L = map(int, input().split())
ans = 0
for i in range(N):
    tmp = L / v
    L = u * tmp

print(L)
