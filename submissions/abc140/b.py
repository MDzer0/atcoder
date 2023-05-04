N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
tmp = -1
for i in range(N):
    ans += b[a[i] - 1]
    if tmp == a[i]:
        ans += c[tmp - 2]
    tmp = a[i] + 1

print(ans)
