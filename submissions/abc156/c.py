N = int(input())
x = list(map(int, input().split()))
ans = 10 ** 18 + 1
for i in range(1, 101):
    total = 0
    for j in x:
        total += (i - j) ** 2
    ans = min(ans, total)

print(ans)
