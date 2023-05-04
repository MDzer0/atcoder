A, B, C = map(int, input().split())
ans = 0

if A == B:
    ans = C
elif A == C:
    ans = B
else:
    ans = A

print(ans)
