N = input()
tmp = len(N)
ans = 0

for i in range(1, int(N) + 1):
    if i < 10:
        ans += 1
    elif 100 <= i and i <= 999:
        ans += 1
    elif 10000 <= i and i <= 99999:
        ans += 1
print(ans)
