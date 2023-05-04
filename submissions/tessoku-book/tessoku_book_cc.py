N = str(input())
ans = 0

for i in range(len(N)):
    if N[-i - 1] == '1':
        ans += 2 ** i
print(ans)
