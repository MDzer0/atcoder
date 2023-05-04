S = int(input())
ans = [0, 0, 10 ** 9, 1]
x = (10 ** 9 - S % 10 ** 9) % 10 ** 9
y = (S + x) // 10 ** 9
ans.append(x)
ans.append(y)
print(*ans)
