N = int(input())
ans = 10 ** 18
for i in range(100):
    if 2 ** i > N:
        break
    b = i
    a = N // (2 ** b)
    c = N - a * 2 ** b
    ans = min(ans, a + b + c)

print(ans)
