A, B = map(int, input().split())
ans = 0
if A >= 13:
    ans = B
elif A >= 6:
    ans = int(B / 2)

print(ans)
