A, B, C = map(int, input().split())
ans = 2 * B
C -= B
if A >= C:
    ans += C
else:
    ans += A + 1

print(ans)
