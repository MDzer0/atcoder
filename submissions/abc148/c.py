import fractions
A, B = map(int, input().split())
tmp = A * B // fractions.gcd(A, B)
print(tmp)
