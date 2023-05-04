N = int(input())
a = list(map(int, input().split()))
for i in range(N - 1):
    print(a[i], end=',')
print(a[-1])
