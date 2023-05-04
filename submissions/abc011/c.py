N = int(input())
n = [int(input()) for _ in range(3)]
dp = [N] * 101
ans = 'NO'
total = 1000
for i in n:
    if N == i:
        print(ans)
        exit()
for i in range(100):
    for j in range(3):
        bflag = True
        for k in n:
            if dp[i] - j - 1 == k:
                bflag = False
                break
        if bflag:
            if dp[i] - j - 1 >= 0:
                total = min(total, dp[i] - j - 1)
    dp[i + 1] = total
    if total == 0:
        ans = 'YES'
        break

print(ans)
