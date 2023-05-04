N = int(input())
p = list(map(int, input().split()))
purasu = [0] * N
for i in range(N):
    purasu[p[i] - 1] = i
a = []
for i in range(1, N + 1):
    a.append(N * i + purasu[i - 1])
b = []
for i in range(N):
    b.append(N * (N - i))

print(*a)
print(*b)
