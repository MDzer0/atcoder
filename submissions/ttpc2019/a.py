A, B, T = map(int, input().split())
s = B - A
ans = 0
for i in range(1, 10 ** 5):
    if T <= B + (s * i):
        ans = B + (s * i)
        break

print(ans)
