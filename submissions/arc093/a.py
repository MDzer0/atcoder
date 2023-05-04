N = int(input())
a = list(map(int, input().split()))
maxa = max(a)
mina = min(a)
a.insert(0, 0), a.append(0)
total = 0
for i in range(N + 1):
    total += abs(a[i] - a[i + 1])

for i in range(N):
        ans = total - abs(a[i] - a[i + 1]) - abs(a[i + 1] - a[i + 2]) + abs(a[i] - a[i + 2])
        print(ans)
