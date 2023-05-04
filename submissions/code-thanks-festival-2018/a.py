T, A, B, C, D = map(int, input().split())
ans = 0
if T >= C:
    ans += D
    T -= C

if T >= A:
    ans += B

print(ans)
