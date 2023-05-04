N = int(input())
A, B, C = map(int, input().split())
ans = 10 ** 5

for i in range(10000):
    for j in range(10000):
        if i + j > 9999 or A * i + B * j > N: break
        tmp = N - (A * i + B * j)
        d, m = divmod(tmp, C)
        if m == 0:
            ans = min(ans, i + j + d)

print(ans)
