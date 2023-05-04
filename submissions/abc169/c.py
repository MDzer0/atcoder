import decimal
A, B = map(decimal.Decimal, input().split())
ans = A * B
print(int(ans))
