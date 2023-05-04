H, N = map(int, input().split())
a = list(map(int, input().split()))

for i in range(N):
        H -= a[i]

if H <= 0:
    print('Yes')
else:
    print('No')
