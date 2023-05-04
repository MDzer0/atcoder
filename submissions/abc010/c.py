txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

ans = 'NO'
for i in range(n):
    tmp1 = pow((abs(x[i] - txa) ** 2 + (abs(y[i] - tya) ** 2)), 0.5)
    tmp2 = pow((abs(x[i] - txb) ** 2 + (abs(y[i] - tyb) ** 2)), 0.5)
    total = tmp1 + tmp2
    if total <= int(T * V):
        ans = 'YES'
        break

print(ans)
