N, T = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)
print((sumA - 1) // T + 1)
