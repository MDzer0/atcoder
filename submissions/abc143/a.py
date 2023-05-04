A, B = map(int, input().split())
ans = 0
tmp = A - (2 * B)

if 0 < tmp:
    ans = tmp
print(ans)
