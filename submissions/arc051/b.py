a, b = 1, 1
K = int(input())
for i in range(K - 1):
    a, b = b, a + b
print(a, b)
