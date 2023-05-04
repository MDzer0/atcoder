N = int(input())
ans = 0

if N & 1:
    print(0)
    exit()
N //= 2
while N:
    N //= 5
    ans += N

print(ans)
