import sys
c = [list(map(int, input().split())) for _ in range(3)]

ans = 'Yes'
for i in range(c[0][0] + 1):
    b = [c[0][0] - i, c[0][1] - i, c[0][2] - i]
    a = [i, abs(b[0] - c[1][0]), abs(b[0] - c[2][0])]
    for j in range(1, 3):
        for k in range(3):
            if c[j][k] != a[j] + b[k]:
                ans = 'No'
                break
        if ans != 'Yes':
            break
    if ans == 'Yes':
        break
    if i != c[0][0]:
        ans = 'Yes'

print(ans)
