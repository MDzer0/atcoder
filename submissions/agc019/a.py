Q, H, S, D = map(int, input().split())
N = int(input())
ans = 0

if N >= 2:
    tmp = N // 2
    ans += (min(Q * 8, H * 4, S * 2, D) * tmp)
if N % 2 != 0:
    ans += min(Q * 4, H * 2, S)

print(ans)
