A, B, C = map(int, input().split())
ans = 'Yes'
if A > C:
    if B > C:
        ans = 'No'
else:
    if B < C:
        ans = 'No'

print(ans)
