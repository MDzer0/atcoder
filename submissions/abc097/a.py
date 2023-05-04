a, b, c, d = map(int, input().split())

ans = ''

if abs(a - c) > d:
    if abs(a - b) <= d and abs(b - c) <= d:
        ans = 'Yes'
    else:
        ans = 'No'
else:
    ans = 'Yes'

print(ans)
