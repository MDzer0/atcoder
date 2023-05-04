N = int(input())
h = list(map(int, input().split()))

for i in range(1, N):
    if h[i] - h[i - 1] >= 1:
        h[i] -= 1

for i in range(1, N):
    if h[i] - h[i - 1] < 0:
        print('No')
        exit()

print('Yes')
