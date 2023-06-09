N = int(input())
A = map(int, input().split())
MOD = 1000000007
ans = 1
cnt = [3 if i == 0 else 0 for i in range(N + 1)]

for a in A:
    ans = ans * cnt[a] % MOD

    cnt[a] -= 1
    cnt[a+1] += 1

print(ans)
