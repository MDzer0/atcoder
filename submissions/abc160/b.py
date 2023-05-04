X = int(input())
a = X // 500
X %= 500
b = X // 5
ans = a * 1000 + b * 5
print(ans)
