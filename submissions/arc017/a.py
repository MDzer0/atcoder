N = int(input())
ans = 'YES'
for i in range(2, N):
    if N % i == 0:
        ans = 'NO'
        break
print(ans)
