A, B, C = map(int, input().split())
bc = B * C
if A > bc:
    A -= A - bc

print(A / B)
