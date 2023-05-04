N, M = map(int, input().split())

total = 0
for i in range(1, N + 1):
    total += i ** 2

print(total % M)
