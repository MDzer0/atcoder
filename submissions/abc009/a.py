N = int(input())
ans = 0
if N % 2:
    ans = int(N / 2) + 1
else:
    ans = int(N / 2)
print(ans)
