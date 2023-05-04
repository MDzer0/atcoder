N, A, B = map(int, input().split())

maxA = min(A, B)
minA = 0
if N - max(A, B) < maxA:
    minA = maxA - (N- max(A, B))
print(maxA, minA)
