N = int(input())
b = list(map(int, input().split()))
a = []

for i in range(N):
    tmp = -1
    for j in range(N - i):
        if b[j] == j + 1:
            tmp = j
            
    if tmp != -1:
        a.append(b.pop(tmp))

if len(a) == N:
    for i in range(N - 1, -1, -1):
        print(a[i])
else:
    print(-1)
