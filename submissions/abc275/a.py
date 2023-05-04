N = int(input())
H = list(map(int, input().split()))
ans = 0
tmp = 0

for i in range(N):
    if tmp < H[i]:
        ans = i + 1
        tmp = H[i]
print(ans)
